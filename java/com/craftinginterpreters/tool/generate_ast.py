import sys
from typing import TextIO


def main() -> None:
    """Main function to generate the AST classes."""
    if len(sys.argv) != 2:
        print("Usage: generate_ast.py <output_directory>")
        sys.exit(65)
    output_dir = sys.argv[1]
    define_ast(
        output_dir,
        "Expr2",
        [
            "Binary   : Expr left, Token operator, Expr right",
            "Grouping : Expr expression",
            "Literal  : Object value",
            "Unary    : Token operator, Expr right",
        ],
    )


def define_ast(output_dir: str, base_name: str, types: list[str]) -> None:
    """Generate the AST classes in Java."""
    path = output_dir + "/" + base_name + ".java"
    with open(path, "w", encoding="utf-8") as fp:
        fp.write("package com.craftinginterpreters.lox;\n")
        fp.write("\n")
        fp.write("import java.util.List;\n")
        fp.write("\n")
        fp.write(f"abstract class {base_name} {{\n")

        define_visitor(fp, base_name, types)

        # The AST classes.
        for type_ in types:
            class_name, fields = [x.strip() for x in type_.split(":")]
            define_type(fp, base_name, class_name, fields)

        # The base accept() method.
        fp.write("  abstract <R> R accept(Visitor<R> visitor);\n")

        fp.write("}\n")


def define_visitor(fp: TextIO, base_name: str, types: list[str]) -> None:
    """Define the visitor interface for the AST."""
    fp.write("  interface Visitor<R> {\n")

    for type_ in types:
        type_name = type_.split(":")[0].strip()
        fp.write(
            f"    R visit{type_name}{base_name}({type_name} {base_name.lower()});\n"
        )
        fp.write("\n")

    fp.write("  }\n")
    fp.write("\n")


def define_type(fp: TextIO, base_name: str, class_name: str, field_list: str) -> None:
    """Define a type in the AST."""
    fp.write(f"  static class {class_name} extends {base_name} {{\n")

    # Constructor
    fp.write(f"    {class_name}({field_list}) {{\n")

    # Store parameters in fields.
    fields = field_list.split(", ")
    for field in fields:
        name = field.split(" ")[1]
        fp.write(f"      this.{name} = {name};\n")

    fp.write("    }\n")

    # Visitor pattern.
    fp.write("\n")
    fp.write("    @Override\n")
    fp.write("    <R> R accept(Visitor<R> visitor) {\n")
    fp.write(f"      return visitor.visit{class_name}{base_name}(this);\n")
    fp.write("    }\n")

    # Fields.
    fp.write("\n")
    for field in fields:
        fp.write(f"    final {field};\n")

    fp.write("  }\n")
    fp.write("\n")


if __name__ == "__main__":
    main()
