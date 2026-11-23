# 材料（materials.bin）を合言葉で暗号化・復号する
# 使い方: python3 kg_crypt.py enc|dec <合言葉ファイル> <入力> <出力>
import sys, os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
mode, pwf, src, dst = sys.argv[1:5]
pw = open(pwf, encoding='utf-8').read().strip().lower().replace('-', '').replace(' ', '').encode()
def key(salt): return PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=600000).derive(pw)
data = open(src, 'rb').read()
if mode == 'enc':
    salt, iv = os.urandom(16), os.urandom(12)
    open(dst, 'wb').write(b'KG1' + salt + iv + AESGCM(key(salt)).encrypt(iv, data, None))
else:
    assert data[:3] == b'KG1', 'format'
    salt, iv = data[3:19], data[19:31]
    open(dst, 'wb').write(AESGCM(key(salt)).decrypt(iv, data[31:], None))
