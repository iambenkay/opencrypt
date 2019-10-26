# opencrypt
### Install
clone this repo:
```sh
git clone https://github.com/iambenkay/opencrypt.git
cd opencrypt
```
### How To
All you need to do is import `crypt.py` and use it's helper functions:

```python
import crypt

crypt.encrypt("Hello World")
# prints the encrypted form of the string

crypt.decrypt(crypt.encrypt("Hello World"))
# prints "Hello World" (by decoding the encrypted form of it)
```

Enjoy!!
