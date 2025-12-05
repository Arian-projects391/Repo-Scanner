# Scan Report: https://github.com/Arian-projects391/Repo-Scanner.git

*Timestamp: Fri Dec  5 05:51:39 2025*

## semgrep
```

Semgrep not installed — skipping.
```

## trufflehog
```

TruffleHog not installed — skipping.
```

## bandit
```
{
  "errors": [],
  "generated_at": "2025-12-05T10:51:39Z",
  "metrics": {
    "/tmp/tmpaw_0r5u4/Repo-Scanner.git/report_summary.py": {
      "CONFIDENCE.HIGH": 0,
      "CONFIDENCE.LOW": 0,
      "CONFIDENCE.MEDIUM": 0,
      "CONFIDENCE.UNDEFINED": 0,
      "SEVERITY.HIGH": 0,
      "SEVERITY.LOW": 0,
      "SEVERITY.MEDIUM": 0,
      "SEVERITY.UNDEFINED": 0,
      "loc": 30,
      "nosec": 0,
      "skipped_tests": 0
    },
    "/tmp/tmpaw_0r5u4/Repo-Scanner.git/scanner.py": {
      "CONFIDENCE.HIGH": 2,
      "CONFIDENCE.LOW": 0,
      "CONFIDENCE.MEDIUM": 0,
      "CONFIDENCE.UNDEFINED": 0,
      "SEVERITY.HIGH": 0,
      "SEVERITY.LOW": 2,
      "SEVERITY.MEDIUM": 0,
      "SEVERITY.UNDEFINED": 0,
      "loc": 61,
      "nosec": 0,
      "skipped_tests": 0
    },
    "_totals": {
      "CONFIDENCE.HIGH": 2,
      "CONFIDENCE.LOW": 0,
      "CONFIDENCE.MEDIUM": 0,
      "CONFIDENCE.UNDEFINED": 0,
      "SEVERITY.HIGH": 0,
      "SEVERITY.LOW": 2,
      "SEVERITY.MEDIUM": 0,
      "SEVERITY.UNDEFINED": 0,
      "loc": 91,
      "nosec": 0,
      "skipped_tests": 0
    }
  },
  "results": [
    {
      "code": "1 import os\n2 import subprocess\n3 import json\n",
      "col_offset": 0,
      "end_col_offset": 17,
      "filename": "/tmp/tmpaw_0r5u4/Repo-Scanner.git/scanner.py",
      "issue_confidence": "HIGH",
      "issue_cwe": {
        "id": 78,
        "link": "https://cwe.mitre.org/data/definitions/78.html"
      },
      "issue_severity": "LOW",
      "issue_text": "Consider possible security implications associated with the subprocess module.",
      "line_number": 2,
      "line_range": [
        2
      ],
      "more_info": "https://bandit.readthedocs.io/en/1.9.2/blacklists/blacklist_imports.html#b404-import-subprocess",
      "test_id": "B404",
      "test_name": "blacklist"
    },
    {
      "code": "10     try:\n11         result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)\n12         return result.stdout, result.stderr\n",
      "col_offset": 17,
      "end_col_offset": 95,
      "filename": "/tmp/tmpaw_0r5u4/Repo-Scanner.git/scanner.py",
      "issue_confidence": "HIGH",
      "issue_cwe": {
        "id": 78,
        "link": "https://cwe.mitre.org/data/definitions/78.html"
      },
      "issue_severity": "LOW",
      "issue_text": "subprocess call - check for execution of untrusted input.",
      "line_number": 11,
      "line_range": [
        11
      ],
      "more_info": "https://bandit.readthedocs.io/en/1.9.2/plugins/b603_subprocess_without_shell_equals_true.html",
      "test_id": "B603",
      "test_name": "subprocess_without_shell_equals_true"
    }
  ]
}
[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None

```

## safety
```

No requirements.txt found for Safety
```

## pip-audit
```

No requirements.txt found for pip-audit
```

## yamllint
```


```

## flawfinder
```
Flawfinder version 2.0.19, (C) 2001-2019 David A. Wheeler.
Number of rules (primarily dangerous function names) in C/C++ ruleset: 222

FINAL RESULTS:


ANALYSIS SUMMARY:

No hits found.
Lines analyzed = 0 in approximately 0.00 seconds (0 lines/second)
Physical Source Lines of Code (SLOC) = 0
Hits@level = [0]   0 [1]   0 [2]   0 [3]   0 [4]   0 [5]   0
Hits@level+ = [0+]   0 [1+]   0 [2+]   0 [3+]   0 [4+]   0 [5+]   0

Dot directories skipped = 1 (--followdotdir overrides)
Minimum risk level = 1

There may be other security vulnerabilities; review your code!
See 'Secure Programming HOWTO'
(https://dwheeler.com/secure-programs) for more information.

Warning: Skipping directory with initial dot /tmp/tmpaw_0r5u4/Repo-Scanner.git/.git

```

## gitleaks
```


    ○
    │╲
    │ ○
    ○ ░
    ░    gitleaks

[90m5:51AM[0m [32mINF[0m 12 commits scanned.
[90m5:51AM[0m [32mINF[0m scan completed in 685ms
[90m5:51AM[0m [31mWRN[0m leaks found: 8

```

## hadolint
```

No Dockerfile found
```

