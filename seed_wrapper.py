---

### 📄 `seed_wrapper.py`

```python
def pause_and_reflect(func):
    def wrapper(*args, **kwargs):
        print("<<pause>>\n<<reflect>>")
        return func(*args, **kwargs)
    return wrapper
