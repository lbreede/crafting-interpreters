JAVAC = javac
JAVA = java
SRC_DIR = com/craftinginterpreters/lox
MAIN_CLASS = com.craftinginterpreters.lox.Lox

.PHONY: build run clean

build:
	$(JAVAC) $(SRC_DIR)/*.java

run: build
	$(JAVA) $(MAIN_CLASS) $(ARGS)

clean:
	find . -name "*.class" -delete
