import random
import time
import truss_chains as chains
from truss.base import truss_config


class RandInt(chains.ChainletBase):
    remote_config = chains.RemoteConfig(
        runtime=chains.Runtime(
            health_checks=truss_config.HealthChecks(
                restart_check_delay_seconds=90,
                restart_threshold_seconds=900,
                stop_traffic_threshold_seconds=111,
            )
        )
    )

    def __init__(
        self, context: chains.DeploymentContext = chains.depends_context()
    ) -> None:
        self._environment = context.environment
        self.environment_name = self._environment.name if self._environment else None
        time.sleep(10)
        self.fail_readiness_checks = False

    def is_healthy(self) -> bool:
        if self.fail_readiness_checks:
            return False
        try:
            self.run_remote(1)
            return True
        except Exception:
            return False

    def run_remote(self, max_value: int) -> int:
        if max_value == 5:
            print("will start to fail health checks")
            self.fail_readiness_checks = True
        else:
            print("will start to succeed health checks")
            self.fail_readiness_checks = False
        rand_int = random.randint(1, max_value)
        return rand_int


@chains.mark_entrypoint
class NEWCustomHealthChecks(chains.ChainletBase):
    remote_config = chains.RemoteConfig(
        runtime=chains.Runtime(
            health_checks=truss_config.HealthChecks(
                restart_check_delay_seconds=100,
                stop_traffic_threshold_seconds=111,
            )
        )
    )

    def __init__(
        self,
        rand_int=chains.depends(RandInt, retries=3),
        context: chains.DeploymentContext = chains.depends_context(),
    ) -> None:
        self._rand_int = rand_int
        self._environment = context.environment
        self.environment_name = self._environment.name if self._environment else None
        self.model_ready = False
        time.sleep(10)
        self.model_ready = True

    def is_healthy(self) -> bool:
        return self.model_ready

    def run_remote(self, max_value: int) -> str:
        num_repetitions = self._rand_int.run_remote(max_value)
        return f"{self.environment_name} " * num_repetitions
