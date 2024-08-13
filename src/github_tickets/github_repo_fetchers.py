from github_tickets.github_repo_fetcher import GithubRepoFetcher


ENV = "dev"

HIGH_ISSUE_LIMIT = 10 if ENV == "dev" else 10_000
MEDIUM_ISSUE_LIMIT = 4 if ENV == "dev" else 5_000
LOW_ISSUE_LIMIT = 2 if ENV == "dev" else 1_000

REPO_FETCHERS = [
    GithubRepoFetcher(
        "microsoft/vscode",
        positive_labels=["bug", "feature-request", "enhancement", "performance", "documentation"],
        negative_labels=["invalid"],
        max_issues=HIGH_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "facebook/react",
        positive_labels=["Type: Bug", "Type: Enhancement", "Type: Documentation"],
        negative_labels=["invalid", "duplicate", "wontfix", "spam"],
        max_issues=LOW_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "nodejs/node",
        positive_labels=["confirmed-bug", "good first issue", "help wanted", "question"],
        negative_labels=["invalid", "duplicate", "wontfix"],
        max_issues=HIGH_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "angular/angular",
        positive_labels=["bug", "feature", "performance", "docs", "PR action: merge"],
        negative_labels=["invalid", "duplicate", "wontfix", "obsolete"],
        max_issues=LOW_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "home-assistant/home-assistant.io",
        positive_labels=["bug", "docs", "enhancement", "feature request"],
        negative_labels=["invalid", "duplicate", "wontfix", "stale"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "home-assistant/core",
        positive_labels=["bug", "feature request", "docs"],
        negative_labels=["invalid", "duplicate", "wontfix", "stale"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "docker/for-win",
        positive_labels=["kind/bug", "kind/enhancement", "kind/documentation"],
        negative_labels=["invalid", "duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "kubernetes/kubernetes",
        positive_labels=["kind/bug", "kind/support", "kind/feature", "kind/enhancement"],
        negative_labels=["triage/duplicate", "triage/not-reproducible", "triage/needs-information"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "ansible/ansible",
        positive_labels=["bug", "docs", "enhancement", "feature request"],
        negative_labels=["invalid", "duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "arduino/Arduino",
        positive_labels=["Type: Bug", "Type: Documentation", "Type: Enhancement"],
        negative_labels=["Invalid", "Duplicate", "Won't Fix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "openstreetmap/openstreetmap-website",
        positive_labels=["bug", "enhancement", "documentation", "good first issue"],
        negative_labels=["invalid", "duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "tarantool/tarantool",
        positive_labels=["bug", "enhancement", "question", "docs"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "magento/magento2",
        positive_labels=["Issue: Confirmed", "Issue: Improvement", "Issue: Feature Request", "Issue: Documentation"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "tensorflow/tensorflow",
        positive_labels=["type:bug", "type:feature", "type:documentation", "stat:awaiting response",
                         "contributions welcome"],
        negative_labels=["type:duplicate", "type:wontfix", "stat:closed"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "flutter/flutter",
        positive_labels=["severe: new feature", "severe: performance", "documentation", "good first issue",
                         "customer: crowd", "customer: end user"],
        negative_labels=["waiting for customer response", "duplicate", "wontfix"],
        max_issues=HIGH_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "apache/spark",
        positive_labels=["bug", "improvement", "documentation", "help wanted", "good first issue"],
        negative_labels=["invalid", "wontfix", "duplicate"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "golang/go",
        positive_labels=["Proposal", "Documentation", "Help Wanted", "Performance"],
        negative_labels=["Duplicate", "Working as Intended", "Won't Fix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "elastic/elasticsearch",
        positive_labels=["bug", "enhancement", "documentation", "good first issue"],
        negative_labels=["duplicate", "stale", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "elastic/kibana",
        positive_labels=["bug", "enhancement", "documentation", "good first issue", "help wanted"],
        negative_labels=["duplicate", "invalid", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "dotnet/roslyn",
        positive_labels=["Bug", "Enhancement", "Documentation", "Help Wanted", "Good First Issue"],
        negative_labels=["Won't Fix", "Duplicate", "Invalid"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "rust-lang/rust",
        positive_labels=["A-bug", "A-enhancement", "A-documentation", "E-easy", "help wanted", "good first issue"],
        negative_labels=["I-duplicate", "I-wontfix", "I-invalid"],
        max_issues=HIGH_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "XX-Net/XX-Net",
        positive_labels=["bug", "enhancement", "documentation", "help wanted"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "dotnet/runtime",
        positive_labels=["bug", "enhancement", "documentation", "help wanted", "good first issue"],
        negative_labels=["duplicate", "won't fix"],
        max_issues=HIGH_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "pytorch/pytorch",
        positive_labels=["bug", "feature", "enhancement", "good first issue", "documentation"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=HIGH_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "dotnet/sdk",
        positive_labels=["bug", "enhancement", "documentation", "help wanted"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "godotengine/godot",
        positive_labels=["bug", "enhancement", "feature", "documentation", "good first issue"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "FortAwesome/Font-Awesome",
        positive_labels=["bug", "enhancement", "feature request", "documentation"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "microsoft/TypeScript",
        positive_labels=["bug", "feature request", "performance", "documentation", "good first issue"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=HIGH_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "Azure/azure-docs",
        positive_labels=["documentation", "bug", "enhancement", "good first issue"],
        negative_labels=["wontfix", "duplicate"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "cockroachdb/cockroach",
        positive_labels=["bug", "enhancement", "feature", "documentation", "good first issue"],
        negative_labels=["wontfix", "duplicate"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "ytdl-org/youtube-dl",
        positive_labels=["bug", "enhancement", "feature", "documentation"],
        negative_labels=["wontfix", "duplicate"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "moby/moby",
        positive_labels=["bug", "enhancement", "documentation", "good first issue", "help wanted"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=HIGH_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "JuliaLang/julia",
        positive_labels=["bug", "enhancement", "documentation", "good first issue"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "ProtonMail/Proton",
        positive_labels=["bug", "enhancement", "feature request", "documentation"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "PowerShell/PowerShell",
        positive_labels=["Issue-Bug", "Issue-Enhancement", "Issue-Documentation", "Help Wanted", "Good First Issue"],
        negative_labels=["Resolution-Won't Fix", "Duplicate"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "dotnet/maui",
        positive_labels=["bug", "enhancement", "documentation", "good first issue", "help wanted"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "tgstation/tgstation",
        positive_labels=["Bug", "Feature Request", "Documentation", "Good First Issue"],
        negative_labels=["Won't Fix", "Duplicate", "Invalid"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "electron/electron",
        positive_labels=["bug", "enhancement", "documentation", "good first issue"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=HIGH_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "typeorm/typeorm",
        positive_labels=["bug", "enhancement", "documentation", "good first issue", "help wanted"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "microsoft/terminal",
        positive_labels=["bug", "enhancement", "feature request", "documentation"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "openssl/openssl",
        positive_labels=["bug", "enhancement", "feature request", "documentation"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "rethinkdb/rethinkdb",
        positive_labels=["bug", "enhancement", "feature request", "documentation", "good first issue"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "hashicorp/terraform",
        positive_labels=["bug", "enhancement", "documentation", "good first issue", "help wanted"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "cocos2d/cocos2d-x",
        positive_labels=["bug", "enhancement", "feature request", "documentation"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "haskell/cabal",
        positive_labels=["bug", "enhancement", "documentation", "good first issue", "help wanted"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "intellij-rust/intellij-rust",
        positive_labels=["bug", "enhancement", "good first issue", "help wanted", "documentation"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "rust-clippy/rust-clippy",
        positive_labels=["bug", "enhancement", "good first issue", "documentation"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "cockroachdb/cockroach",
        positive_labels=["bug", "enhancement", "feature request", "documentation"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "OpenRA/OpenRA",
        positive_labels=["bug", "enhancement", "documentation", "good first issue"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "godotengine/godot",
        positive_labels=["bug", "enhancement", "feature", "documentation", "good first issue"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "mpv-player/mpv",
        positive_labels=["bug", "enhancement", "documentation", "feature request", "good first issue"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "moby/moby",
        positive_labels=["bug", "enhancement", "documentation", "good first issue", "help wanted"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=HIGH_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "home-assistant/frontend",
        positive_labels=["bug", "enhancement", "documentation", "good first issue"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "vuejs/vue",
        positive_labels=["bug", "feature request", "documentation", "question", "good first issue", "improvement"],
        negative_labels=["wontfix", "duplicate", "invalid"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "flask/flask",
        positive_labels=["bug", "enhancement", "documentation", "help wanted", "good first issue"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "fastai/fastai",
        positive_labels=["bug", "enhancement", "documentation", "good first issue", "help wanted"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "scikit-learn/scikit-learn",
        positive_labels=["bug", "enhancement", "documentation", "good first issue"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "laravel/framework",
        positive_labels=["bug", "enhancement", "documentation", "good first issue"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "rails/rails",
        positive_labels=["bug", "enhancement", "feature request", "documentation", "good first issue"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "tensorflow/models",
        positive_labels=["type:bug", "type:feature", "type:enhancement", "good first issue", "stat:awaiting response"],
        negative_labels=["type:duplicate", "type:wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "python/cpython",
        positive_labels=["bug", "enhancement", "feature request", "documentation", "good first issue"],
        negative_labels=["duplicate", "wontfix"],
        max_issues=MEDIUM_ISSUE_LIMIT
    ),
    GithubRepoFetcher(
        "django/django",
        positive_labels=["bug", "enhancement", "documentation", "easy pickings", "good first issue",
                         "needs clarification"],
        negative_labels=["duplicate", "wontfix", "invalid"],
        max_issues=MEDIUM_ISSUE_LIMIT
    )
]
