def test_can_import():
    import serial
    serial


def test_can_import_main():
    import serial.__main__ as main
    main
