ROOT_DIR := $(dir $(realpath $(lastword $(MAKEFILE_LIST))))

HASHQUERY_VERSION := $(shell sed -n 's/version = "\([^"]*\)"/\1/p' pyproject.toml)

PUBLIC_REPO_URL := git@github.com:hashboard-hq/hashquery.git
PUBLIC_REPO_DIR := ~/code/hashquery-public
PUBLIC_REPO_SYNC_FILES := src/ docs/ README.md CONTRIBUTING.md CHANGELOG.md LICENSE pyproject.toml .github/ .gitignore
PUBLIC_REPO_BRANCH_NAME := $(shell whoami)/release-$(HASHQUERY_VERSION)

all:: clean build deploy github_pr

clean::
	@echo "Cleaning dist..."
	rm -rf dist

# Builds the deployable Python artifacts to `dist/`
build:: clean
	@echo "Building the package..."
	rm __init__.py
	python3 -m pip install --upgrade build && \
	  python3 -m build
	touch __init__.py

# Deploys the Python package to pip from `dist/`
deploy:: build
	@echo "Deploying the package to pip..."
	python3 -m pip install --upgrade twine && \
	  python3 -m twine upload dist/*

# Syncs the contents of this directory with the public Github,
# pushing a new branch which can be PR'd for merge
github_pr::
	@echo "Commiting latest file tree to public GitHub"
	@echo "Syncing public repo..."
	@if [ ! -d $(PUBLIC_REPO_DIR) ]; then \
		git clone $(PUBLIC_REPO_URL) $(PUBLIC_REPO_DIR); \
	else \
		cd $(PUBLIC_REPO_DIR) && git checkout main && git pull; \
	fi

	@echo "Copying files..."
	@cd $(PUBLIC_REPO_DIR) && \
		git checkout -b $(PUBLIC_REPO_BRANCH_NAME)
	@for file in $(PUBLIC_REPO_SYNC_FILES); \
		do cp -r $(ROOT_DIR)/$$file $(PUBLIC_REPO_DIR)/$$file; \
	done

	@echo "Publishing branch $(PUBLIC_REPO_BRANCH_NAME)..."
	cd $(PUBLIC_REPO_DIR) && \
		git add . && \
		git commit -m "$(HASHQUERY_VERSION)" && \
		git push -u origin $(PUBLIC_REPO_BRANCH_NAME)
