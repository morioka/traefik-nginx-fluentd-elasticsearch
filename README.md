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