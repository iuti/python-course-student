# Python Course Materials

中学生向けPython授業の生徒用教材です。

このリポジトリには、授業で使用する説明と練習用コードだけを収録しています。模範解答や個人の学習記録は含みません。

## 現在の教材

| 回 | 内容 | フォルダ |
|---:|---|---|
| 第6回 | VS Codeへの移行とリストの基本 | [`lesson06_list`](lesson06_list/) |

## 使い方

### 初めて使う場合

1. [`setup/vscode_setup.md`](setup/vscode_setup.md)を見て準備する
2. 画面上部の **Code → Download ZIP** を押す
3. ZIPファイルを展開する
4. VS Codeで、このフォルダを開く
5. 授業回のREADMEを上から読む

### Gitを習った後

最初の1回だけ、リポジトリを複製します。

```bash
git clone <このリポジトリのURL>
```

次回以降は、教材フォルダで更新を取得します。

```bash
git pull
```

## 大切なルール

配布された教材を直接書き換えるのではなく、自分の作業用フォルダへコピーしてから編集してください。

```text
Documents/
├─ PythonMaterials/  この教材
└─ PythonWork/       自分が編集するプログラム
```

## 実行環境

- Python 3
- Visual Studio Code
- Microsoft Python拡張機能

外部ライブラリは使用しません。

## 過去のColab教材

### 第2回：if・else・input

- [生徒用ノートをColabで開く](https://colab.research.google.com/github/iuti/python-course-student/blob/main/past_colab/python_lesson02_if_student_60min.ipynb)
- 講師用ノートは模範解答を含むため非公開で管理しています

### 第3回：for文

- [生徒用ノートをColabで開く](https://colab.research.google.com/github/iuti/python-course-student/blob/main/past_colab/python_lesson03_for_student_60min.ipynb)
- 講師用ノートは模範解答を含むため非公開で管理しています

### 第4回：while文

- [生徒用ノートをColabで開く](https://colab.research.google.com/github/iuti/python-course-student/blob/main/past_colab/python_lesson04_while_student_60min.ipynb)
- 講師用ノートは模範解答を含むため非公開で管理しています
