from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello!"}


@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}!"}


instrumentator = Instrumentator(
    should_instrument_requests_inprogress=True,  # in-progress 메트릭 수집 활성화
    inprogress_name="http_requests_inprogress",  # 메트릭 이름 지정
    inprogress_labels=True,  # handler, method 라벨도 함께 붙여줌
)

# Prometheus 메트릭 자동 수집 + /metrics 엔드포인트 노출
# instrument(app): 모든 요청에 대해 응답시간, 요청수, 상태코드 등을 자동으로 측정하도록 설정
# expose(app): /metrics 라는 경로를 만들고, 거기서 측정된 값을 prometheus가 읽을 수 있는 텍스트 형식으로 보여준다.
instrumentator.instrument(app).expose(app)
