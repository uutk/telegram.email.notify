# Оповещения в каналах и группах Telegram от популярных ресурсов: YouTube, Facebook, Одноклассники и т.п. Решение с открытым исходным кодом.

Вы можете получать в Telegram оповещения от любого ресурса, который может отправлять оповещения на заданный вами email. Для этого нужно:

- убедиться, что на этом ресурсе вы включили оповещения на ваш почтовый ящик
- получить у бота Telegram EmailGateBot специальный адрес емейл
- включить в вашем почтовом ящике пересылку оповещений на этот емейл

Чтобы убрать из пересылаемых сообщений HTML разметку и сделать сообщения краткими и информативными, EmailGateBot использует свою функцию автоматического преобразования текста.
EmailGateBot отправляет содержимое получаемых оповещений на специальный сайт и публикует в нужном канале/группе Telegram ответ от этого сайта.
Таким способом EmailGateBot может обрабатывать оповещения от [FaceBook](fb/guide.md), [YouTube](youtube/guide.md), Одноклассники, [Яндекс Деньги](ym/guide.md) и некоторых других.
От какого именно ресурса поступило оповещение, EmailGateBot определяет по адресу отправителя. Например, оповещения от Youtube рассылаются с адреса noreply@youtube.com.

Код сайта, который обрабатывает содержимое оповещений, написан на Python/Flask и [доступен на Github](https://github.com/vb64/telegram.email.notify/blob/master/README-ru.md).
Вы можете свободно использовать данный код, чтобы развернуть собственный сайт обработки оповещений на своем хосте. Или предложить свой код (Pull Request на Github), который будет обрабатывать нужные вам оповещения на [существующем хосте EmailGateBot](faq.md).

Кроме показа оповещений от популярных ресурсов, @EmailGateBot умеет делать много полезных вещей. Можете ознакомиться с [подробным описанием](guide.md) возможностей EmailGateBot.
