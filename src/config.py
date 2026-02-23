from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Settings:
    project_root: Path = Path(__file__).resolve().parents[1]
    data_dir: Path = project_root / "data"
    raw_dir: Path = data_dir / "raw"
    dataset_dir: Path = data_dir / "dataset"

    # SEC 要求带联系方式的 UA（建议你换成你的邮箱）
    user_agent: str = "BANA275-NLP-StudentProject/1.0 (contact: ruofay3@uci.edu)"

    # 保守限流：0.2s ~= 5 req/s
    sleep_seconds: float = 0.2

settings = Settings()