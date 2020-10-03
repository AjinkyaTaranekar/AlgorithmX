# Contributing guidelines

## Before contributing

Welcome to [AlgorithmX](https://github.com/AjinkyaTaranekar/AlgorithmX)! Before sending your pull requests, make sure that you **read the whole guidelines**. If you have any doubt on the contributing guide, please feel free to [state it clearly in an issue](https://github.com/AjinkyaTaranekar/AlgorithmX/issues/new).

## Contributing

### Contributor

We are very happy that you consider implementing algorithms and data structure for others! This repository is referenced and used by learners from all over the globe. Being one of our contributors, you agree and confirm that:

- You did your work - no plagiarism allowed
  - Any plagiarized work will not be merged.
- You submitted work fulfils or mostly fulfils our styles and standards
- No PR will be accepted with fixing of minor white spaces or spams

**New implementation** is welcome! For example, new solutions for a problem, different representations for a graph data structure or algorithm designs with different complexity.

**Improving comments** and **writing proper tests** are also highly welcome.

### Contribution

We appreciate any contribution, from solving a small problem to implementing complex algorithms. Please read this section if you are contributing your work.

Please help us keep our issue list small by adding fixes: #{$ISSUE_NO} to the commit message of pull requests that resolve open issues. GitHub will use this tag to auto close the issue when the PR is merged.

#### Coding Style

We want your work to be readable by others; therefore, we encourage you to note the following:

- **Use consistent indentation**
There is no right or wrong indentation that everyone should follow. The best style, is a consistent style. Once you start competing in large projects you’ll immediately understand the importance of consistent code styling.
- **Follow the DRY Principle**
DRY stands for “Don’t Repeat Yourself. The same piece of code should not be repeated over and over again.
- **Avoid Deep Nesting**
Too many levels of nesting can make code harder to read and follow.
For example:

```
if (a) {
   …
  if (b) {
      …
    if (c) {
        …
        …
        …
    }
  }
}
```
Can be written as:

```
if (a) {
   return …
}
if (b) {
   return …
}
if (c) {
   return …
}
```
- **Limit line length**
Long lines are hard to read. It is a good practice to avoid writing horizontally long lines of code.
- **File and folder structure**
You should avoid writing all of your code in one of 1-2 files. That won’t break your app but it would be a nightmare to read, debug and maintain your application later.
Keeping a clean folder structure will make the code a lot more readable and maintainable.
- **Naming conventions**
Use of proper naming conventions is a well known best practice. Is a very common issue where developers use variables like X1, Y1 and forget to replace them with meaningful ones, causing confusion and making the code less readable.
- **Keep the code simple**
The code should always be simple. Complicated logic for achieving simple tasks is something you want to avoid as the logic one programmer implemented a requirement may not make perfect sense to another. So, always keep the code as simple as possible.
For example:

```
if (a < 0 && b > 0 && c == 0) {
   return true;
} else {
   return false;
```
Can be written as:
```
return a < 0 && b > 0 && c == 0;
```
- Avoid importing external libraries for basic algorithms. Only use those libraries for complicated algorithms. If used mention them in comments to resolve **hows?**

#### Other Standard While Submitting Your Work


- Most importantly,
  - **Be consistent in the use of these guidelines when submitting.**
  - **Happy coding!**
