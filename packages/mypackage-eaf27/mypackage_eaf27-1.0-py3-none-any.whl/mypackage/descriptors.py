class ShowAccess:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = instance.__dict__.get(self.name)
        print(f"Get {self.name} = {value}")
        return value

    def __set__(self, instance, value):
        print(f"Set {self.name} = {value}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        value = instance.__dict__.get(self.name)
        print(f"Delete {self.name} = {value}")
        instance.__dict__.pop(self.name, None)

if __name__ == "__main__":
    print(f"{__file__} executed as script.")