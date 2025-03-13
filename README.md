# 91160-ocr-server

## Run

1. 安装依赖

```shell
pip install -r requirements.txt
```

2. 启动程序

```shell
uvicorn main:app --reload
```

3. 识别API

```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/ocr' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'image=iVBORw0KGgoAAAANSUhEUgAAAFoAAAAeCAYAAACsYQl4AAADq0lEQVR42u2Y30d7cRjHJ0mSZNLFrpIuki5mkiS76CqTTLpIkszUTBdJ0kUySdLFLvoDutjFJJNdTbKLSbpKksxMkkwmSZIk8Xy9H9/P7Ltv5+ycs9M6p87Dh9V5Ps85n9fn8/z4PDaypCpisxBYoC3Qlligfw7oj48P2tnZIY/HQw6Hg+rq6qilpYWGhoYoFospf7HNxkO3hfy1Vzpqa2vJbrdTT08PbW5u0uvrq2rbh4eHND09TR0dHdTY2MgDv30+Hx0dHekPOpPJUFdXl+SiMLxeL729vRkGdOno7+9X9H2Qx8dHPkDlbI6NjdHLy4s+oK+urvhkwDBOx97eHuXzef5obMDq6irV19fz8/Hx8W8D/ZkHPjw80P7+fuH7t7a2ytp7fn6m7u5u1ofHrq+v08XFBQOFV+B3KBSi5uZm1nG5XLLeonilvb29bHBiYoI//jNJJBJUU1PDenA3I4Aulmg0yjpOp7OsvcnJycKhwoGSkpubG+rs7GRdhJeKQAMgDLW1tZWNcX6/n3WHh4cNB/rp6Yl1GhoaZPUuLy/5wMAD7u7uFHk74jbmYK5m0NgppS53enrKiWJpaclwoAENOk1NTbJ6CwsLrLeysqL4/fPz8zwHczWDFq5xfn5eVTB629ve3madgYEBWT3EW+idnJwofj+qDxGrNYMWAR8JwmygEepKk3UkEpG1JZImqg6lgoQrEqdm0KhFYUQqCRoJdLmBHPIV631/f+c5uFdoBi12GMnEbKCxcFysRkZGuMRTs141J/r+/p7ntLa2agctYtbZ2ZmpY7RS0RKjU6lUoRzUDDoYDLKRcDhcVhcJs729XTL7mgH04uIi21peXlZddUhVWzY1u4XqA7FITubm5lgXrmpW0Ol0mmtiFAG3t7f/PZ+ZmeHDl81m+e/r62tOtJiDG2NFN8O+vj5eSCAQkNQ5ODgoJJJkMmla0MUXL9wic7ncP89QHuIZ4KKaEeXv1NRU5VdwxGfcqGDQ7XbzbRHJAnd/7CLczQi9jtisl0elgrIQ8RY2kRzX1tZ4nfg/+jsbGxuFdoPYELnGkqqV4sSKjCw1RkdHq9q9E2D1AlwsAIfOnJKyEfXz7u6uPqBFYY7dRZMJxhEqUNKgtxGPx6vi6p+B1dtDSm996D2jtQCvxhUe7WLE6uPjY+7sCW8eHBzUB/R3yVedWr0EjSXEdalKxWYGsEaFqyqHWKf2l4D+yXC/FfRPCwmGAv0bwVYV9G+Ha8ryzuzyB6byb/lCgWdcAAAAAElFTkSuQmCC'
```

```json
{
  "code": 200,
  "msg": "ok",
  "data": "cipq"
}
```

## Docker

1. 拉取镜像

```shell
docker pull ghcr.io/pengpan/91160-ocr-server:latest
```

2. 启动容器

```shell
docker run --name 91160-ocr-server \
-p 8000:8000 \
-e TZ=Asia/Shanghai \
--restart=always \
-d 91160-ocr-server:latest
```