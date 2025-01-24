import my_base_tkinter_app


def test_imports():
    all_exposed = my_base_tkinter_app.__all__

    for exposed_attribute_name in all_exposed:
        assert hasattr(my_base_tkinter_app, exposed_attribute_name) is True
