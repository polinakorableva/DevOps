from fastapi import FastAPI

#создание приложения
app = FastAPI (
    title="Test Manager API",
    description='Учим ляляля',
    version='0.1.0'
)

#две ассинхронные функции
@app.get("/") #приложение app должно обрабатывать метод get по пути /. Обработка - функция снизу
async def root():
    """Простой эндопинт - проверка работоспособности"""
    return {"message": "Hellow from FastAPI!"}

@app.get('/health')
async def health_chek():
    """Health check для миниторинга"""
    return {"status": "healthy", 'version': "0.1.0"}

# запуск: python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload, где unicorn нужен для запуска приложения, host - IP адресс (0.0.0.0 - любой), порты по умолчанию обычно
# потом тест в терминале curl -X  GET http://localhost:8000/health или просто в браузере URL
#можно ещё такой URL - http://127.0.0.1:8000/health, где 127.0.0.1 - адресс моего компа, тогда на другом компе не запустится
#или http://0.0.0.0:8000/health - любой IP