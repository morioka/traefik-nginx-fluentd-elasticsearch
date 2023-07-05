# traefik-nginx-fluentd-elasticsearch

コンテナで構築したNginxのアクセスログをFluentdでElasticsearchに送る。

# Quick Start

```bash
git clone https://github.com/v1tam1nb2/traefik-nginx-fluentd-elasticsearch.git
cd traefik-nginx-fluentd-elasticsearch
docker-compose build
docker-compose up -d
curl http://localhost/service-a.html
curl http://localhost/service-b.html
```

# ログの確認(Kibana)

- http://localhost:5601

# 参考

- [Create a data view](https://www.elastic.co/guide/en/kibana/master/data-views.html)
- [docker-composeでリバースプロキシとしてtraefikを使う](https://cloudandbuild.jp/blog/article-7)


# 2023-07-05

- fluent-plugin-sqlite3 を試してみた
  - データベースファイルとそのディレクトリへの読み書き権限が必要
  - カラム数の上限が2000くらいで打ち止め。
- elasticsearch
  - https://boomin.yokohama/archives/50
  - https://help.liferay.com/hc/ja/articles/360020885111-DXP%E3%81%AB%E3%82%88%E3%82%8BElasticsearch%E3%81%AE%E3%82%A4%E3%83%B3%E3%83%87%E3%83%83%E3%82%AF%E3%82%B9%E3%81%AE%E7%B7%8F%E3%83%95%E3%82%A3%E3%83%BC%E3%83%AB%E3%83%89%E6%95%B0%E3%81%AE%E5%A4%89%E6%9B%B4%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6#:~:text=%E7%8F%BE%E5%9C%A8%E3%81%AE%E6%9C%80%E5%A4%A7%E3%83%95%E3%82%A3%E3%83%BC%E3%83%AB%E3%83%89%E6%95%B0%E3%81%AF7500%E3%81%A7%E3%81%99%E3%80%82
  - field数上限値を引き上げることはできる。パフォーマンスへの影響はわからんが。

