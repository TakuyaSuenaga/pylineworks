#!/usr/bin/env python3

import pytest
from tests import env
import pylineworks


api = pylineworks.api(env.CLIENT_ID, env.CLIENT_SECRET, env.SERVICE_ACCOUNT,
                      env.PRIVATE_KEY, "board")


@pytest.fixture(scope="module")
def created_board():
    board = api.boards.boards.create(
        boardName="Test Create Board",
        description="Test Create Board",
    )
    yield board
    api.boards.boards.delete([board.boardId])


class TestBoards:
    def test_create(self, created_board):
        assert created_board
        assert created_board.boardId

    def test_all(self):
        boards = api.boards.boards.all()
        assert boards is not None
        assert len(boards) > 0

    def test_get(self, created_board):
        board = api.boards.boards.get(created_board.boardId)
        assert board is not None
        assert board.boardId == created_board.boardId

    def test_update(self, created_board):
        created_board.description = "updated description"
        ret = api.boards.boards.update(created_board)
        assert ret
        board = api.boards.boards.get(created_board.boardId)
        assert board.description == "updated description"
