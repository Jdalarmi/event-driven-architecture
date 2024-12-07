from consumer import Consumer


def main():
    consumer = Consumer(topic='events')
    consumer.consume()


if __name__ == '__main__':
    main()