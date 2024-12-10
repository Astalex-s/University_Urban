import asyncio


async def start_strongman(name, power):
    # количнство шаров для каждого участника
    num_bulls = 5
    # задержка обратно пропорциональная силе power
    delay = 1 / power
    print(f'Силач {name} начал соревнования.')
    for bull in range(1, num_bulls + 1):
        await asyncio.sleep(delay)
        print(f'Силач {name} поднял {bull}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3


if __name__ == '__main__':
    asyncio.run(start_tournament())
