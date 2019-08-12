# Django_09_简述QQ登陆过程

## Question
简述 QQ 登陆过程

第一步是请求 qq 服务器返回一个 qq 登录的界面;

第二步是通过扫码或账号登陆进行验证，qq 服务器返回给浏览器一个 code 和____,利用这个 code 通过本地服务器去向 qq 服务器获取 access_token 覆返回给本地服务器，凭借____再向 qq 服务器获取用户的____

第三步是判断用户是否是第一次qq登录，如果不是的话直接登录返回的____给用户，对没有绑定过本网站的用户，对 openid 进行加密生成 token 进行绑定
        
%!A. state, access_token, openid, jwt-token!%

%!B. openid, state, access_token, jwt-token!%

%!C. state, access_token, jwt-token, openid!%

%!D. openid, state, jwt-token, access_token!%

----

## Answer
@!A!@

----

## Analysis

qq 登录，在我们的项目中分为了三个接口，

第一个接口是请求 qq 服务器返回一个qq登录的界面;

第二个接口是通过扫码或账号登陆进行验证，qq 服务器返回给浏览器一个 code 和 state ,利用这个 code 通过本地服务器去向qq服务器获取 access_token 覆返回给本地服务器，凭借 access_token 再向 qq 服务器获取用户的 openid(openid 用户的唯一标识)

第三个接口是判断用户是否是第一次 qq 登录，如果不是的话直接登录返回的 jwt-token 给用户，对没有绑定过本网站的用户，对 openid 进行加密生成 token 进行绑定