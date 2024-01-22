# Логика работы системы
После создания новой рассылки, если текущее время больше времени начала и меньше времени окончания, то должны быть выбраны из справочника все клиенты, которые указаны в настройках рассылки, и запущена отправка для всех этих клиентов.
Если создается рассылка со временем старта в будущем, то отправка должна стартовать автоматически по наступлению этого времени без дополнительных действий со стороны пользователя системы.
По ходу отправки сообщений должна собираться статистика (см. описание сущности «сообщение» и «логи» выше) по каждому сообщению для последующего формирования отчетов.
Внешний сервис, который принимает отправляемые сообщения, может долго обрабатывать запрос, отвечать некорректными данными, на какое-то время вообще не принимать запросы. Нужна корректная обработка подобных ошибок. Проблемы с внешним сервисом не должны влиять на стабильность работы разрабатываемого сервиса рассылок.

# System operation logic
After creating a new mailing, if the current time is greater than the start time and less than the end time, then all clients that are specified in the mailing settings must be selected from the directory, and sending to all these clients must be started.
If a mailing is created with a start time in the future, then the sending should start automatically when this time arrives without additional actions on the part of the system user.
As messages are sent, statistics should be collected (see the description of the “message” entity and “logs” above) for each message for subsequent generation of reports.
An external service that receives sent messages may take a long time to process the request, respond with incorrect data, or not accept requests at all for some time. We need correct handling of such errors. Problems with the external service should not affect the stability of the developed mailing service.