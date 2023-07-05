from fluent import sender
# for remote fluent
logger = sender.FluentSender('sqlite3', host='localhost', port=24224)

logger.emit('follow', {'Afrom': 'userA', 'Ato': 'userB'})
