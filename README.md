# kot_auto

kot自動入力

## 仮想環境の作り方

pipenvを使用する

### 初期化

    $ pipenv install

### パッケージのインストール

    $ pipenv install xxx

## pyinstallerでexeファイルを作成する方法

### 手順

1. 仮想環境のシェルを起動

    ```
    $ pipenv shell
    ```

2. specファイルを作成

    ``` 
    $ pyi-makespec ./main.py --name kot_auto --onefile
    ```

3. exeファイル作成

    ```
    $ pyinstaller kot_auto.spec --noconfirm
    ```
