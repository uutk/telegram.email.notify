# EmailGateBot FAQ

## Насколько надежный хостинг у бота? Насколько велик шанс, что бот перестанет работать в самый ответственный момент?

Бот реализован на платформе Google App Engine Standard Environment и использует в качестве хостнига [датацентр Google в городе Council Bluffs](https://www.google.com/about/datacenters/inside/locations/council-bluffs/), штат Айова, США. Оборудование этого датацентра также обеспечивает работу штатных служб Google (Поиск, Почта, Карты и т.д.).

Так что шанс отказа бота по вине хостинга равен шансу прекращения работы служб Google в соответствующем регионе США. Большой или маленький это шанс, каждый пользователь бота может оценить самостоятельно.

## Вечером я забыл разрешить постинг в мой канал для нового адреса email. Утром я нажал кнопку, чтобы разрешить постинг, и увидел сообщение 'обработано ранее'. Что произошло?

Запрос на обработку входящей почты активен в течение одного часа. Если вы не ответили на запрос в течение часа, то входящий емейл игнорируется.

## Как изменить адреса, которым разрешено постить в чат? Я хочу удалить адрес.

Когда на емейл-адрес чата впервые поступает сообщение с нового емейл-адреса, бот спрашивает у вас, что делать с письмами с этого адреса. Если вы нажимаете кнопку меню "Разрешить навсегда" или "Запретить навсегда", то данный емейл-адрес попадает соответственно в "белый" или "черный" список адресов. Последующие письма с адресов из "белого" списка публикуются автоматически, а письма с адресов из "черного" списка игнорируются. Если вы в дальнейшем изменили свое первоначальное решение и хотите запретить какому-либо адресу из "белого" списка автоматически публиковать сообщения, вам нужно сделать следующее.

Отправить команду `/start` в приват с ботом, выбрать группу, где нужно удалить емейл-адрес, выбрать из меню "Управление белым списком" (в самом конце меню, прокрутить колесиком мыши), выбрать нужный емейл-адрес из списка адресов, из меню выбрать "Удалить".

Управление "черным" списком аналогично управлению "белым" списком.
