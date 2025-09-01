# kot_auto

kot自動入力

## 事前準備

### Google Chrome のインストール

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get update
sudo apt-get install -y ./google-chrome-stable_current_amd64.deb
```

### 対応する ChromeDriver をダウンロード

```bash
CHROME_VERSION=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+\.\d+')
wget https://storage.googleapis.com/chrome-for-testing-public/$CHROME_VERSION/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
sudo mv chromedriver-linux64/chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver
```

### 不要ファイルの削除

```bash
rm google-chrome-stable_current_amd64.deb
rm chromedriver-linux64.zip
rm -rf chromedriver-linux64
```

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
