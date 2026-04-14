from pathlib import Path
from playwright.sync_api import sync_playwright

OUT_DIR = Path(r"D:\dev\caracore-pdv-releases\docs\wiki\assets\images\manual-upgrade-java21")
URL = "http://localhost:8080/"

SHOTS = [
    ("01-precheck-terminal.png", None),
    ("02-backup-criado.png", "#dores"),
    ("03-upgrade-go.png", "#beneficios"),
    ("04-validacao-aplicacao.png", "#pronto-2026"),
    ("05-rollback-ok.png", "footer"),
]


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        page = browser.new_page(viewport={"width": 1600, "height": 1000})
        page.goto(URL, wait_until="networkidle")

        for file_name, selector in SHOTS:
            if selector:
                locator = page.locator(selector)
                if locator.count() > 0:
                    locator.first.scroll_into_view_if_needed()
                    page.wait_for_timeout(700)
            page.screenshot(path=str(OUT_DIR / file_name), full_page=False)
            print(f"saved: {file_name}")

        # Captura extra da tela de representantes, se disponível
        page.goto("http://localhost:8080/wiki/representantes.html", wait_until="networkidle")
        page.screenshot(path=str(OUT_DIR / "06-representantes.png"), full_page=False)
        print("saved: 06-representantes.png")

        browser.close()


if __name__ == "__main__":
    main()
