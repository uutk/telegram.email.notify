# -*- coding: utf-8 -*-

source1 = """
Тилигульский лиман

Одесский Клуб Рыболовов Здравствуйте, VinsT! 
мирон 2 опубликовал комментарий в тему, Тилигульский лиман 


мирон 2 опубликовал(а): 14 часа назад, Ігор сказал: 
Можно связывать канатом использованые шины и притапливать в лимане. Их быстро освоят мидии и другие жители лимана. 
А с экологией как? Перейти к сообщению 

Одесский Клуб Рыболовов Вы получили это письмо, потому что вы подписаны на Тема "Тилигульский лиман". 
Отказаться от получения этих писем? Отписаться или Настройка уведомлений . 
Одесский Клуб Рыболовов, одесса, одесса, одесса, 65000
"""

result1 = """Одесский Клуб Рыболовов: 
Тилигульский лиман

мирон 2 опубликовал(а): 14 часа назад, Ігор сказал: 
Можно связывать канатом использованые шины и притапливать в лимане. Их быстро освоят мидии и другие жители лимана. 
А с экологией как?"""

source2 = """
Три карася

Одесский Клуб Рыболовов Здравствуйте, VinsT! 
Anutka_Odessa_Mayaki опубликовал комментарий в тему, Три карася 


Anutka_Odessa_Mayaki опубликовал(а): http://fishingclub.od.ua/forums/index.php?/topic/20432-открытый-турнир-по-карпфишингу-открытие-сезона-2018-на-рк-три-карася/ page=3 
Приглашаем всех желающих принять участие в турнире "Один на один с трофеем"! Перейти к сообщению 

Одесский Клуб Рыболовов Вы получили это письмо, потому что вы подписаны на Тема "Три карася". 
Отказаться от получения этих писем? Отписаться или Настройка уведомлений . 
Одесский Клуб Рыболовов, одесса, одесса, одесса, 65000
"""

result2 = """Одесский Клуб Рыболовов: 
Три карася

Anutka_Odessa_Mayaki опубликовал(а): http://fishingclub.od.ua/forums/index.php?/topic/20432-открытый-турнир-по-карпфишингу-открытие-сезона-2018-на-рк-три-карася/ page=3 
Приглашаем всех желающих принять участие в турнире "Один на один с трофеем"!"""

source3 = """
Ответ в теме 'Рыбалка на озерах и ставках'

Уважаемый(ая) VinsT,

dimon777 только что ответил в теме, на которую Вы подписались, - Рыбалка на озерах и ставках - в разделе Охота и рыбалка Одесский форум.

Эта тема расположена по адресу:
http://forumodua.com/showthread.php?t=1548612&goto=newpost

Размещенное сообщение:
***************
Вот нашел еще один интересный водоем на просторах и-нета Чистоводное в Белгород-Днестровском районе https://www.youtube.com/watch?v=7wJEKTmW1pE
Может кто был там, поделитесь инфой.
***************


Также могут быть и другие сообщения, но Вы не будете получать уведомления, пока снова не посетите форум.

С наилучшими пожеланиями,
Одесский форум

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Отказ от подписки:

Чтобы отказаться от получения рассылки по этой теме, пожалуйста, перейдите на страницу:
http://forumodua.com/subscription.php?do=removesubscription&type=thread&subscriptionid=13057535&auth=bc52182903810d701d0ff06c2a122e2d

Чтобы отказаться от получения рассылок по ВСЕМ темам, пожалуйста, перейдите на страницу:
http://forumodua.com/subscription.php?do=viewsubscription&folderid=all
"""

result3 = """dimon777 только что ответил в теме, на которую Вы подписались, - Рыбалка на озерах и ставках - в разделе Охота и рыбалка Одесский форум.

Эта тема расположена по адресу:
http://forumodua.com/showthread.php?t=1548612&goto=newpost

Размещенное сообщение:
***************
Вот нашел еще один интересный водоем на просторах и-нета Чистоводное в Белгород-Днестровском районе https://www.youtube.com/watch?v=7wJEKTmW1pE
Может кто был там, поделитесь инфой.
***************

Также могут быть и другие сообщения, но Вы не будете получать уведомления, пока снова не посетите форум."""

broken1 = """
Ответ в теме 'Рыбалка на озерах и ставках'

Уважаемый(ая) VinsT,

dimon777 только что ответил - Рыбалка на озерах и ставках - в разделе Охота и рыбалка Одесский форум.

"""

broken2 = """Ответ в теме 'Рыбалка на озерах и ставках' dimon777 только что ответил в теме, на которую Вы подписались, - Рыбалка на озерах и ставках - в разделе Охота и рыбалка Одесский форум.
"""

broken3 = """
Ответ в теме 'Рыбалка на озерах и ставках'

Уважаемый(ая) VinsT,

dimon777 только что ответил в теме, на которую Вы подписались, - Рыбалка на озерах и ставках - в разделе Охота и рыбалка Одесский форум.

Эта тема расположена по адресу:
http://forumodua.com/showthread.php?t=1548612&goto=newpost

Размещенное сообщение:
***************
Вот нашел еще один интересный водоем на просторах и-нета Чистоводное в Белгород-Днестровском районе https://www.youtube.com/watch?v=7wJEKTmW1pE
Может кто был там, поделитесь инфой.
***************


С наилучшими пожеланиями,
Одесский форум
"""

result4 = """dimon777 только что ответил в теме, на которую Вы подписались, - Рыбалка на озерах и ставках - в разделе Охота и рыбалка Одесский форум.

Эта тема расположена по адресу:
http://forumodua.com/showthread.php?t=1548612&goto=newpost

Размещенное сообщение:
***************
Вот нашел еще один интересный водоем на просторах и-нета Чистоводное в Белгород-Днестровском районе https://www.youtube.com/watch?v=7wJEKTmW1pE
Может кто был там, поделитесь инфой.
***************

С наилучшими пожеланиями,
Одесский форум"""

source5 = """
Тилигульский лиман

Одесский Клуб Рыболовов Здравствуйте, VinsT! 
мирон 2 опубликовал комментарий в тему, Тилигульский лиман 


мирон 2 опубликовал(а): 14 часа назад, Ігор сказал: 
Можно связывать канатом использованые шины и притапливать в лимане. Их быстро освоят мидии и другие жители лимана. 
А с экологией как?

Перейти к сообщению 

Одесский Клуб Рыболовов Вы получили это письмо, потому что вы подписаны на Тема "Тилигульский лиман". 
Отказаться от получения этих писем? Отписаться или Настройка уведомлений . 
Одесский Клуб Рыболовов, одесса, одесса, одесса, 65000
"""

result5 = """Одесский Клуб Рыболовов: 
Тилигульский лиман

мирон 2 опубликовал(а): 14 часа назад, Ігор сказал: 
Можно связывать канатом использованые шины и притапливать в лимане. Их быстро освоят мидии и другие жители лимана. 
А с экологией как?"""
