import asyncio

async def async_task(no):
    print(f"Starting async task {no}...")
    await asyncio.sleep(2)  # Simulate a long-running task
    print(f"Async task {no} completed!")

async def main():
    await asyncio.gather(
        async_task(1),
        async_task(2),
        async_task(3)
    )

# Run the async task
asyncio.run(main())