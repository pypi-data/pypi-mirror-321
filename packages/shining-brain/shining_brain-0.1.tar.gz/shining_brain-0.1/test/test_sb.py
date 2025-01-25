from shining_brain.sb import create_parser


def test_parse():
    args = create_parser(["merge-pdf", "a", "b"])
    assert args.command == "merge-pdf"
    assert args.src == "a"
    assert args.dest == "b"
