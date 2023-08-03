[![Build Status](https://app.travis-ci.com/cobusc/django-protected-media.svg?branch=master)](https://app.travis-ci.com/cobusc/django-protected-media)


Django Protected Media
======================

Django Protected Mediaは、機密性の高いメディアを保護された方法で管理するDjangoアプリです。

メディアは別のファイルシステムの場所に保存されるだけでなく、
アクセスするには認証を要求されるようになります。

このアプリケーションではDjangoが認証を行い、Nginxのようなウェブサーバがファイルを提供するようなセットアップが可能です。

Quick start
-----------

1. 次のように `pip` でパッケージをインストールするします:
```bash
pip install django-protected-media
```

2. 次のように INSTALLED_APPS の設定に "protected_media" を追加します:
```python
INSTALLED_APPS = [
    ...
    'protected_media.apps.ProtectedMediaConfig',
]
```

3. プロジェクトの `urls.py` に次のように URLconf をインクルードします:
```
path('protected/', include('protected_media.urls')),
```

4. デフォルトの設定を調整する必要がある場合は、`settings.py` に以下の設定を追加します:
```python
PROTECTED_MEDIA_ROOT = "%s/protected/" % BASE_DIR
PROTECTED_MEDIA_URL = "/protected"
PROTECTED_MEDIA_SERVER = "nginx"  # デフォルトは "django" です
PROTECTED_MEDIA_LOCATION_PREFIX = "/internal"  # nginxの設定で使用されるプレフィックス
PROTECTED_MEDIA_AS_DOWNLOADS = False  # Content-Dispositionヘッダーを含めるか
```

5. モデルで新しいフィールドクラスを使用します:
```python
from protected_media.models import ProtectedImageField, ProtectedFileField

def SomeModel(models.Model):
    document = ProtectedFileField(upload_to="uploads/")
    picture = ProtectedImageField(upload_to="uploads/")
    # Files will be stored under PROTECTED_MEDIA_ROOT + upload_to
```

概要
--------

Django は以下の定義に基づいてメディアを管理します:
```python
BASE_DIR = "/some/application/dir/"
MEDIA_ROOT = "%s/media/" % BASE_DIR
MEDIA_URL = "/media/"
```

ファイルフィールドと画像フィールドは、通常次のように定義されます:
```python
document = models.FileField(upload_to="uploads/")
picture = models.ImageField(upload_to="uploads/")
# Files will be stored under MEDIA_ROOT + upload_to
```

典型的な本番環境では、`nginx`（または他のサーバー）にメディアを提供させます:
```
# Publicly accessible media
location ^~ /media/ {
    alias /some/application/dir/media
}
```

これは、メディアが一般にアクセス可能である場合にはうまく機能します。しかし、もしメディアが保護されるべきなら、 Django がメディアへのリクエストをログインした (あるいはもっと厳しい基準の) ユーザだけに許可すべきかどうかをチェックする方法が必要です。

`protected_media` アプリケーション
--------------------------------
`protected_media` アプリケーションは以下のように構成されます
* 新しい `settings.py` 属性の追加
* カスタマイズされたFileSystemStorageクラス,
* 保護されたメディアURLのカスタムハンドラ
* `nginx`やそれに類するものでサービスを提供する場合は、ウェブサーバの追加設定を行う。

保護されたメディアは、一般にアクセス可能なメディアとは異なる物理的な場所に保存されます。以下の設定は `settings.py` で指定できます:
```python
PROTECTED_MEDIA_ROOT = "/some/application/dir/protected/"
PROTECTED_MEDIA_URL = "/protected"
PROTECTED_MEDIA_SERVER = "nginx"  # Defaults to "django"
PROTECTED_MEDIA_LOCATION_PREFIX = "/internal"  # Prefix used in nginx config
```

保護が必要なファイルや画像フィールドを定義する場合、`protected_media` アプリケーションが提供するクラスのいずれかを使用します:
* `ProtectedFileField`
* `ProtectedImageField`

保護されたファイルフィールドと画像フィールドは、通常次のように定義されます:
```python
document = ProtectedFileField(upload_to="uploads/")
picture = ProtectedImageField(upload_to="uploads/")
# Files will be stored under PROTECTED_MEDIA_ROOT + upload_to
```

これらのクラスはカスタム・ストレージのバックエンド `ProtectedFileSystemStorage` を持ち、保護されたメディアに関連するファイルシステムの場所とURLを管理します

`nginx`を使用する場合は、次のように設定を更新する必要があります:
```
# Publicly accessible media
location /media  {
    alias /some/application/dir/media;
}

# Protected media
location /internal  {
    internal;
    alias /some/application/dir/protected;
}
```

