.PHONY: clean publish publish-test

dist/: pyproject.toml $(shell find src -type f -name '*.py')
	rm -rf dist/ build/ *.egg-info
	uv build

clean:
	rm -rf dist/ build/ *.egg-info

publish: dist/
	uv run twine upload dist/*

publish-test: dist/
	uv run twine upload --repository testpypi dist/* 
