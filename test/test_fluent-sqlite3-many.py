from fluent import sender
# for remote fluent
logger = sender.FluentSender('sqlite3', host='localhost', port=24224)


#d = { f"{k}": 2*k for k in range(500)}
d = { f"{k}": 2*k for k in range(800)}
d = { f"{k}": 2*k for k in range(900)}  # OK
d = { f"{k}": 2*k for k in range(1000)} # NG

d = { f"{k}": 2*k for k in range(6000)} 
#logger.emit('follow', {'Afrom': 'userA', 'Ato': 'userB'})
logger.emit('testtest', d)
