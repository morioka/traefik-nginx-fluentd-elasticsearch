# https://docs.fluentd.org/output/elasticsearch
FROM fluent/fluentd:v1.16.0-debian-1.0

USER root

RUN mkdir -p /fluentd/db-sqlite3

# FluentdとElasticsearchを連携させるためのプラグインをインストール
RUN gem install fluent-plugin-elasticsearch --no-document --version 5.2.4
RUN gem install fluent-plugin-sqlite3

#USER fluent
