.PHONY: setup test spec-check

setup:
	docker build -t chimera-test .

test:
	docker run --rm chimera-test

spec-check:
	@echo "Spec check not implemented yet. You can run custom scripts here."
