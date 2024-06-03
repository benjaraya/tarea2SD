from flask import Flask, jsonify, request
from kafka import KafkaProducer
import asyncio
import requests
import json



async def send_one():
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092')
    await producer.start()
    try:
        await producer.send_and_wait("my_topic", b"Super message")
    finally:
        await producer.stop()

asyncio.run(send_one())