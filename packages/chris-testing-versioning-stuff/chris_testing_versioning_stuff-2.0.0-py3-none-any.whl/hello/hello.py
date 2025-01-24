def main(name: str = "python-template-test") -> str:
    if not isinstance(name, str):
        raise NotImplementedError("Only strings are supported!")
    return f"Hello {name}!"


if __name__ == "__main__":
    main()
