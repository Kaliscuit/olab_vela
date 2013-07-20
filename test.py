from model import user
import config


xiaozhui = user.User(config.db, 'yuhanjian@yaho0ssso.com')
xiaozhui.nickname = 'xiaozhuiiii'
xiaozhui.password = 'password'
xiaozhui.save()

print xiaozhui.email
