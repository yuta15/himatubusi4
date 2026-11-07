from .examples import example_requests
from .service import ApplyService


def main() -> None:
    service = ApplyService()
    for request in example_requests():
        print(service.apply(request))
        print("-" * 60)


if __name__ == "__main__":
    main()
