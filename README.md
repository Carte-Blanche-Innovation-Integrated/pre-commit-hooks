# Using pre-commit-hooks with pre-commit
Add this to your `.pre-commit-config.yaml`

```YAML
-   repo: 
    rev: 1.0.0 # Use the ref you want to point at
    hooks:
    -   id: migration-files-checker
    # -   id: ...
```
# Hooks Available
`migration-files-checker`

Prevent Django migration files from being committed if their serial numbers are the same.



