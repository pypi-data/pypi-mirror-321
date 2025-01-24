from contextlib import contextmanager
import logging
import os
import socket
import sys
import uuid
import sentry_sdk
from enum import Enum
from typing import List, Dict
import requests


class Feature(Enum):
    REDTEAMING = "redteaming"
    SYNTHESIZER = "synthesizer"
    EVALUATION = "evaluation"
    GUARDRAIL = "guardrail"
    BENCHMARK = "benchmark"
    UNKNOWN = "unknown"


TELEMETRY_DATA_FILE = ".deepeval_telemtry.txt"

#########################################################
### Context Managers ####################################
#########################################################


def get_unique_id(file_path=TELEMETRY_DATA_FILE):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = f.read().strip().split("\n")
            unique_id = data[0] if len(data) > 0 else str(uuid.uuid4())
    else:
        unique_id = str(uuid.uuid4())
        # Initialize the file with the new unique ID and unknown feature
        with open(file_path, "w") as f:
            f.write(f"{unique_id}\n{Feature.UNKNOWN.value}")
    return unique_id


def get_last_feature(file_path=TELEMETRY_DATA_FILE):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = f.read().strip().split("\n")
            last_feature = data[1] if len(data) > 1 else Feature.UNKNOWN.value
            return (
                Feature(last_feature)
                if last_feature in Feature._value2member_map_
                else Feature.UNKNOWN
            )
    else:
        return Feature.UNKNOWN


def set_last_feature(feature: Feature, file_path=TELEMETRY_DATA_FILE):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = f.read().strip().split("\n")
            unique_id = data[0]  # Keep the existing unique_id
    else:
        unique_id = str(uuid.uuid4())

    with open(file_path, "w") as f:
        f.write(f"{unique_id}\n{feature.value}")


#########################################################
### Telemetry Config ####################################
#########################################################


def telemetry_opt_out():
    return os.getenv("DEEPEVAL_TELEMETRY_OPT_OUT") == "YES"


def blocked_by_firewall():
    try:
        socket.create_connection(("www.google.com", 80))
        return False
    except OSError:
        return True


def get_anonymous_public_ip():
    try:
        response = requests.get("https://api.ipify.org", timeout=5)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        pass
    return None


anonymous_public_ip = None

if not telemetry_opt_out():
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
        OTLPSpanExporter,
    )

    anonymous_public_ip = get_anonymous_public_ip()
    sentry_sdk.init(
        dsn="https://5ef587d58109ee45d6544f3657efdd1f@o4506098477236224.ingest.sentry.io/4506098479136768",
        profiles_sample_rate=1.0,
        traces_sample_rate=1.0,  # For performance monitoring
        send_default_pii=False,  # Don't send personally identifiable information
        attach_stacktrace=False,  # Don't attach stack traces to messages
        default_integrations=False,  # Disable Sentry's default integrations
    )

    # Set up the Tracer Provider
    trace.set_tracer_provider(TracerProvider())
    tracer_provider = trace.get_tracer_provider()

    # New Relic License Key and OTLP Endpoint
    NEW_RELIC_LICENSE_KEY = "1711c684db8a30361a7edb0d0398772cFFFFNRAL"
    NEW_RELIC_OTLP_ENDPOINT = "https://otlp.nr-data.net:4317"
    otlp_exporter = OTLPSpanExporter(
        endpoint=NEW_RELIC_OTLP_ENDPOINT,
        headers={"api-key": NEW_RELIC_LICENSE_KEY},
    )

    # Add the OTLP exporter to the span processor
    span_processor = BatchSpanProcessor(otlp_exporter)
    tracer_provider.add_span_processor(span_processor)

    logging.getLogger("opentelemetry.exporter.otlp").setLevel(logging.CRITICAL)

    # Create a tracer for your application
    tracer = trace.get_tracer(__name__)


if (
    os.getenv("ERROR_REPORTING") == "YES"
    and not blocked_by_firewall()
    and not os.getenv("TELEMETRY_OPT_OUT")
):

    def handle_exception(exc_type, exc_value, exc_traceback):
        print({"exc_type": exc_type, "exc_value": exc_value})
        sentry_sdk.capture_exception(exc_value)
        sys.__excepthook__(exc_type, exc_value, exc_traceback)

    sys.excepthook = handle_exception


#########################################################
### Context Managers ####################################
#########################################################


@contextmanager
def capture_evaluation_run(type: str):
    if not telemetry_opt_out():
        with tracer.start_as_current_span(f"Ran {type}") as span:
            span.set_attribute("user.unique_id", get_unique_id())
            if anonymous_public_ip:
                span.set_attribute("user.public_ip", anonymous_public_ip)
            set_last_feature(Feature.EVALUATION)
            yield span
    else:
        yield


@contextmanager
def capture_metric_type(metric_name: str, _track: bool = True):
    if not telemetry_opt_out() and _track:
        with tracer.start_as_current_span(metric_name) as span:
            span.set_attribute("user.unique_id", get_unique_id())
            if anonymous_public_ip:
                span.set_attribute("user.public_ip", anonymous_public_ip)
            yield span
    else:
        yield


@contextmanager
def capture_synthesizer_run(
    method: str, max_generations: int, num_evolutions: int, evolutions: Dict
):
    if not telemetry_opt_out() and max_generations is not None:
        with tracer.start_as_current_span(f"Invoked synthesizer") as span:
            if anonymous_public_ip:
                span.set_attribute("user.public_ip", anonymous_public_ip)
            span.set_attribute("user.unique_id", get_unique_id())
            span.set_attribute("method", method)
            span.set_attribute("max_generations", max_generations)
            span.set_attribute("evolutions", num_evolutions)
            for evol, value in evolutions.items():
                span.set_attribute(f"evolution.{evol.value}", 1)
            set_last_feature(Feature.SYNTHESIZER)
            yield span
    else:
        yield


@contextmanager
def capture_red_teamer_run(
    attacks_per_vulnerability_type: int,
    vulnerabilities: List,
    attack_enhancements: Dict,
):
    if not telemetry_opt_out():
        with tracer.start_as_current_span(f"Invokved redteamer") as span:
            if anonymous_public_ip:
                span.set_attribute("user.public_ip", anonymous_public_ip)
            span.set_attribute("user.unique_id", get_unique_id())
            span.set_attribute(
                "attacks_per_vulnerability", attacks_per_vulnerability_type
            )
            for vuln in vulnerabilities:
                for types in vuln.get_types():
                    span.set_attribute(f"vulnerability.{types.value}", 1)
            for enhancement, value in attack_enhancements.items():
                span.set_attribute(
                    f"attack_enhancement.{enhancement.value}", value
                )
            set_last_feature(Feature.REDTEAMING)
            yield span
    else:
        yield


@contextmanager
def capture_guardrails(guards: List[str]):
    if not telemetry_opt_out():
        with tracer.start_as_current_span(f"Ran guardrails") as span:
            if anonymous_public_ip:
                span.set_attribute("user.public_ip", anonymous_public_ip)
            span.set_attribute("user.unique_id", get_unique_id())
            for guard in guards:
                span.set_attribute(f"vulnerability.{guard}", 1)
            set_last_feature(Feature.GUARDRAIL)
            yield span
    else:
        yield


@contextmanager
def capture_benchmark_run(benchmark: str, num_tasks: int):
    if not telemetry_opt_out():
        with tracer.start_as_current_span(f"Ran benchmark") as span:
            if anonymous_public_ip:
                span.set_attribute("user.public_ip", anonymous_public_ip)
            span.set_attribute("user.unique_id", get_unique_id())
            span.set_attribute("benchmark", benchmark)
            span.set_attribute("num_tasks", num_tasks)
            set_last_feature(Feature.BENCHMARK)
            yield span
    else:
        yield


@contextmanager
def capture_login_event():
    if not telemetry_opt_out():
        with tracer.start_as_current_span(f"Login") as span:
            last_feature = get_last_feature()
            if anonymous_public_ip:
                span.set_attribute("user.public_ip", anonymous_public_ip)
            span.set_attribute("user.unique_id", get_unique_id())
            span.set_attribute("last_feature", last_feature.value)
            span.set_attribute("completed", True)
            yield span
    else:
        yield
