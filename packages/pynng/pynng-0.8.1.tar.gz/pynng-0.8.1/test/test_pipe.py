"""
Let's test up those pipes
"""


import time

import pytest

import pynng
from _test_util import wait_pipe_len

addr = "inproc://test-addr"


def test_pipe_gets_added_and_removed():
    with pynng.Pair0(listen=addr) as s0, pynng.Pair0() as s1:
        assert len(s0.pipes) == 0
        assert len(s1.pipes) == 0
        s1.dial(addr)
        wait_pipe_len(s0, 1)
        wait_pipe_len(s1, 1)
    wait_pipe_len(s0, 0)
    wait_pipe_len(s1, 0)


def test_close_pipe_works():
    with pynng.Pair0() as s0, pynng.Pair0() as s1:
        # list of pipes that got the callback called on them
        cb_pipes = []

        def cb(pipe):
            cb_pipes.append(pipe)

        # first add callbacks, before listening and dialing.  The callback just adds
        # the pipe to cb_pipes; but this way we can ensure the callback got called.
        s0.add_post_pipe_remove_cb(cb)
        s1.add_post_pipe_remove_cb(cb)
        s0.listen(addr)
        s1.dial(addr)
        wait_pipe_len(s0, 1)
        wait_pipe_len(s1, 1)
        p0 = s0.pipes[0]
        p1 = s1.pipes[0]
        pipe0 = s0.pipes[0]
        pipe0.close()
        # time out in 5 seconds if stuff dosen't work
        timeout = time.monotonic() + 5.0
        while len(cb_pipes) < 2 and time.monotonic() < timeout:
            time.sleep(0.0005)
        if time.monotonic() > timeout:
            raise TimeoutError(
                "Pipe close callbacks were not called; pipe close doesn't work?"
            )
        # we cannot assert the length of cb_pipes is 2 because the sockets might have
        # reconnected in the meantime, so we can only assert that the pipes that
        # *should* have been closed *have* been closed.
        assert p0 in cb_pipes and p1 in cb_pipes


def test_pipe_local_and_remote_addresses():
    with pynng.Pair0(listen=addr) as s0, pynng.Pair0(dial=addr) as s1:
        wait_pipe_len(s0, 1)
        wait_pipe_len(s1, 1)
        p0 = s0.pipes[0]
        p1 = s1.pipes[0]
        local_addr0 = p0.local_address
        remote_addr0 = p0.remote_address
        local_addr1 = p1.local_address
        remote_addr1 = p1.remote_address
        assert str(local_addr0) == addr.replace("tcp://", "")
        assert str(local_addr0) == str(remote_addr1)
        # on Windows, the local address is 0.0.0.0:0
        assert str(local_addr1) == str(remote_addr0)


def test_pre_pipe_connect_cb_totally_works():
    with pynng.Pair0(listen=addr) as s0, pynng.Pair0() as s1:
        called = False

        def pre_connect_cb(_):
            nonlocal called
            called = True

        s0.add_pre_pipe_connect_cb(pre_connect_cb)
        s1.dial(addr)
        wait_pipe_len(s0, 1)
        wait_pipe_len(s1, 1)
        assert called


def test_closing_pipe_in_pre_connect_works():
    with pynng.Pair0(listen=addr) as s0, pynng.Pair0() as s1:
        s0.name = "s0"
        s1.name = "s1"
        pre_connect_cb_was_called = False
        post_connect_cb_was_called = False

        def pre_connect_cb(pipe):
            pipe.close()
            nonlocal pre_connect_cb_was_called
            pre_connect_cb_was_called = True

        def post_connect_cb(pipe):
            nonlocal post_connect_cb_was_called
            post_connect_cb_was_called = True

        s0.add_pre_pipe_connect_cb(pre_connect_cb)
        s0.add_post_pipe_connect_cb(post_connect_cb)
        s1.add_pre_pipe_connect_cb(pre_connect_cb)
        s1.add_post_pipe_connect_cb(post_connect_cb)

        s1.dial(addr)
        later = time.monotonic() + 5
        while later > time.monotonic():
            if pre_connect_cb_was_called:
                break
            # just give other threads a chance to run
            time.sleep(0.0001)
        assert pre_connect_cb_was_called
        wait_pipe_len(s0, 0)
        wait_pipe_len(s1, 0)
        assert not post_connect_cb_was_called


def test_post_pipe_connect_cb_works():
    with pynng.Pair0(listen=addr) as s0, pynng.Pair0() as s1:
        post_called = False

        def post_connect_cb(pipe):
            nonlocal post_called
            post_called = True

        s0.add_post_pipe_connect_cb(post_connect_cb)
        s1.dial(addr)

        later = time.time() + 10
        while later > time.time():
            if post_called:
                break
        assert post_called


def test_post_pipe_remove_cb_works():
    with pynng.Pair0(listen=addr) as s0, pynng.Pair0() as s1:
        post_called = False

        def post_remove_cb(pipe):
            nonlocal post_called
            post_called = True

        s0.add_post_pipe_remove_cb(post_remove_cb)
        s1.dial(addr)
        wait_pipe_len(s0, 1)
        wait_pipe_len(s1, 1)
        assert not post_called

    later = time.time() + 10
    while later > time.time():
        if post_called:
            break
    assert post_called


def test_can_send_from_pipe():
    with pynng.Pair0(listen=addr) as s0, pynng.Pair0(dial=addr) as s1:
        wait_pipe_len(s0, 1)
        s0.send(b"hello")
        assert s1.recv() == b"hello"
        s0.send_msg(pynng.Message(b"it is me again"))
        assert s1.recv() == b"it is me again"


@pytest.mark.trio
async def test_can_asend_from_pipe():
    with pynng.Pair0(listen=addr) as s0, pynng.Pair0(dial=addr) as s1:
        wait_pipe_len(s0, 1)
        await s0.asend(b"hello")
        assert await s1.arecv() == b"hello"
        await s0.asend_msg(pynng.Message(b"it is me again"))
        assert await s1.arecv() == b"it is me again"


def test_bad_callbacks_dont_cause_extra_failures():
    called_pre_connect = False

    def pre_connect_cb(pipe):
        nonlocal called_pre_connect
        called_pre_connect = True

    with pynng.Pair0(listen=addr) as s0:
        # adding something that is not a callback should still allow correct
        # things to work.
        s0.add_pre_pipe_connect_cb(8)
        s0.add_pre_pipe_connect_cb(pre_connect_cb)
        with pynng.Pair0(dial=addr) as _:
            wait_pipe_len(s0, 1)
            later = time.time() + 10
            while later > time.time():
                if called_pre_connect:
                    break
            assert called_pre_connect
