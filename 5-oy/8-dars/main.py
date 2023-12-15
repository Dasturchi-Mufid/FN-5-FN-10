
""" Context manager """

# class Smth:

#     cls_elements = []

#     def __init__(self):
#         self.elements = []
    
#     def __enter__(self):
#         return self
    
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type is not None:
#             print(f"An exception of type {exc_type} occurred with message: {exc_value}")
#             self.elements.clear()
#         else:
#             print("Exiting the context successfully")
#             Smth.cls_elements.append(self.elements)
    
#     def append(self,data):
#         self.elements.append(data)


from contextlib import contextmanager

@contextmanager
def my_context_manager():
    elements = []
    correct_elements = []
    print("Konteksga kirish")
    try:
        yield elements
    except Exception as e:
        print(f"Xatolik: {e}")
        elements.clear()
    finally:
        correct_elements = elements
        print(correct_elements)

with my_context_manager() as value:
    value.append(5)
    value.append('s')
    raise ValueError("Xatolik")
