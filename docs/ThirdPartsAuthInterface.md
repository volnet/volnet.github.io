单点登录-第三方系统验证
===================

> 标签：登录/修改密码/重置密码

> 本工作首次完成时间于：2016-03-25


基本概要
-------

在过去的几年里，我们提供了单点登录的图形化界面，实现用户的登录功能。随着业务的拓展，为了提升单点登录系统的服务能力，我们不仅期望能够通过传统界面来访问系统，还希望能够有更多的访问方式，如自定义的用户界面、跨设备的访问能力、丰富的登录体验等登录场景。

我们将现有的系统进行了一般性抽象，在不改变原有功能特性、安全特性的前提下，实施了相关的接口。

文档目的
-------

本文档将协助您了解相关的技术条件及限制。您可以借助本文档设计您的系统。

接口特性
-------

1. 仅支持http POST方式请求
2. 不同接口返回不同参数，提供统一的SSOMessage消息体格式进行返回。
3. 接口返回消息体中包含用于用户提示的消息，如“密码错误”、“发送成功”等信息，默认情况下可以使用它进行用户提示。
4. 接口返回消息体中包含固定的错误编码，成功==0，其他值表示存在错误，具体含义可以参考错误列表。
5. 仅基于**内网**环境的接口访问方式，保证了在不需要增加外网的防火墙策略的情况下的接口可用性。

安全特性
-------

1. 仅提供**内网**环境的数据校验
2. 基于安全**IP授信**的原则进行认证，使用前需要先进行申请
3. 提供同等于UI界面几乎相同的安全参数

访问地址（SSOHost）
-----------------

1. 测试环境（dev）：sso4dev.wanda-dev.cn
2. 测试环境（pub）：sso4pub.wanda-dev.cn
3. 生产环境：sso.wanda.cn

> 后文中使用ssoHost代表以上访问地址。

> 前端页面可以使用集团网站群下的其他站点访问，如wandafilm.com，因以上接口为后台接口，请直接使用集团域。

> 如需在外网使用接口，请通过**应用系统服务器**发起相应的请求，如果接口需要被暴露到前端页面，请尝试自行封装接口。

> 在整体设计过程中，请务必保证用户界面的安全性设计。业务系统将为整个项目包括调用该接口之后所产生的所有安全问题负责。（我们只对内部系统提供相应的接口，而这些接口可能是***协议共享***的，因此它并不具备***最终安全性***。

通用接口 - 图形验证码接口（API/CAPTCAT.ashx）
----------------------------------------

- 调用说明：

```
GET/POST http://<ssoHost>/API/CAPTCAT.ashx 
```

- 功能说明：

调用该接口可以生成图形验证码。为了统一的安全标准，我们制定自己的图形验证码规则，只有从我们的图形验证码接口获取的图形验证码可以通过后续的调用。

该调用会自动生成图形验证码的图形部分，并将图形直接以base64的方式返回。

使用该接口的用户，只需要直接将该图形信息作为<img>标签的内容，进行显示即可。

关于img直接显示base64可以参考：https://en.wikipedia.org/wiki/Data_URI_scheme

- 请求参数：

无

- 返回值：

``` xml
<SSOMessage>
     <ResultCode></ResultCode>
     <ResultMessageCN></ResultMessageCN>
     <ResultMessageEN></ResultMessageEN>
     <Content>
          <Image>
               <ImageType>data:image/png;base64/url</ImageType>
               <ImageSrcOrContent>xxxx</ImageSrcOrContent>
               <Width></Width>
               <Height></Height>
               <Unit>px</Unit>
          </Image>
          <VerifyInfo>xxxx</VerifyInfo>
     </Content>
</SSOMessage>
```

**ImageType：**图像类型，目前仅提供`data:image/png;base64`类型的值。未来可能提供url形式的值。

**ImageSrcOrContent：**图像内容，如果类型是data:image/png;base64，则此处输出是**图像的base64值**。如果类型为url，则此处输出是具体图像的url。

**Width：**图像宽度，数字

**Height：**图像高度，数字

**Unit：**图像长宽单位

**VerifyInfo：**用户需要将该值传回用于验证，该值内含有校验信息、有效期等信息，该值只能被使用一次，如果重复使用同一个值进行校验，相关验证接口将返回错误。

- 设计建议：

我们不仅提供了图像的内容，还提供了图像的宽度和高度用于您进行显示和设计，默认情况下请您使用这些值。

建议如果用户任何一次请求出错之后，都通过JavaScript脚本重新刷新图形验证码，并提供手动的选项，允许用户在看不清图像的情况下自己刷新图形验证码。

通用接口 - 异步验证码接口（API/PreAsyncVerifyCode.ashx）
---------------------------------------------------

- 调用说明：

```
POST http://<ssoHost>/API/PreAsyncVerifyCode.ashx

参数：UserId=xxxx
```

- 功能说明：

通过该接口可以返回用户是否需要异步验证码的功能，以及用户究竟支持哪种验证码类型。

在实际的使用过程中，我们发现在部分情况下，异步验证码成为了阻碍用户注册的一个障碍。原因通常是由于用户的手机无法接收到验证码短信，这可能不是由用户操作造成的。为此我们设计了可以针对用户进行是否启用异步验证码的开关，管理员有权操作该开关，而我们设计的界面则需要提前获取这样的信息，以决定是否向用户显示异步验证码的相关表单。

- 请求参数：

**UserId：**用户名，传递用户登录所使用的用户名即可。

- 返回值：

```
<SSOMessage>
     <ResultCode></ResultCode>
     <ResultMessageCN></ResultMessageCN>
     <ResultMessageEN></ResultMessageEN>
     <Content>
          <NeedAsyncVerify>true/false</NeedAsyncVerify>
          <SupportedAsyncVerifyTypes>SMS;EMAIL</SupportedAsyncVerifyTypes>
     </Content>
</SSOMessage>
```

**NeedAsyncVerify：**是否需要异步验证码，值为true/false。

**SupportedAsyncVerifyTypes：**支持的异步验证码类型，SMS/EMAIL分别代表短信/电子邮件。

- 设计建议：

我们建议在首次加载页面的时候，调用该接口，以确定是否向用户显示异步验证码相关表单。

通用接口 - 异步验证码接口（API/AsyncVerifyCode.ashx）
------------------------------------------------

- 调用说明：

```
POST http://<ssoHost>/API/AsyncVerifyCode.ashx

参数：UserId=xxxx&ActionType=xxxx&AsyncVerifyType=xxxx
```

- 功能说明：

之所以称之为异步验证码，主要是因为它采用的是从另外一个信道传输验证码，发送该验证码请求的服务程序将无法获取对应的验证码相关信息。只有当最终用户通过对应的形式获得该验证码后，才可正确通过验证。

调用该接口，将向用户发送指定格式的验证码，用户需要在规定的时间内填写该验证码后方可通过后续认证。

验证码类型可能是短信或邮件，目前仅提供短信验证码，系统会根据**主数据平台**提供的人员信息，将短信发送到指定用户。如果用户无法收到短信，有可能是因为短信号码不对、短信被运营商拦截、智能手机设置了垃圾短信屏蔽等功能。

- 请求参数：

**UserId：**用户名，传递用户登录所使用的用户名即可。

**ActionType：**ChangePassword / ResetPassword，目前系统被设计为按照不同的类型，发送不同类型的消息内容，且占用不同的系统资源。比如有一个业务规则是，每个用户每天输错的验证码数量不得多于5次，而此处则根据不同的ActionType，分别享有5次的限额。

**AsyncVerifyType：**验证码发送形式，SMS/EMAIL分别代表短信/电子邮件。

- 返回值：

```
<SSOMessage>
     <ResultCode></ResultCode>
     <ResultMessageCN></ResultMessageCN>
     <ResultMessageEN></ResultMessageEN>
     <Content>
          <DelayedSendTimeOutSetting>60</DelayedSendTimeOutSetting>
          <UserTimeLeft>xx</UserTimeLeft>
     </Content>
</SSOMessage>
```

**DelayedSendTimeOutSetting：**每次发送的最小时间间隔，单位是秒。

**UserTimeLeft：**用户可以再次发送调用本接口发送验证码的时间间隔，单位是秒。

- 设计建议：

在调用该接口之前，首先要确认用户是否需要发送异步验证码，这个信息由PreAsyncVerifyCode接口提供。

如果用户调用完该接口后，接口的返回文字会包含正确的用户提示，如果没有特殊需求，请将其直接显示给用户。

如果用户调用完该接口，再未满再次发送间隔时间范围内又一次调用了该接口（频繁调用），则该接口会返回对应的错误消息，并且包含了提示用户再间隔多少秒才可以发送的信息。如果没有特殊要求，请直接将该结果反馈给用户。

可以借助**DelayedSendTimeOutSetting**参数，在首次调用后，在用户界面上使用JavaScript进行倒计时显示，以免用户多次提交，并禁用发送验证码的按钮，直到用户可以再次发送后，再启用该按钮，以提高用户体验。

认证接口（AuthUser.ashx）
-----------------------

- 调用说明：
- 功能说明：
- 请求参数：
- 返回值：
- 设计建议：

修改/重置密码接口（ChangePassword.ashx）
---------------------------------------

- 调用说明：
- 功能说明：
- 请求参数：
- 返回值：
- 设计建议：

返回值
-------

