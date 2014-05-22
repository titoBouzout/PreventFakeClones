\*[Sublime Text 3+][] **Package. Install via an updated version of**
[Package Control 2+][]**. Just** DON'T\*\* install manually.

# Description

**Prevent Corruption** [1] is a simple Sublime Text 3 plug-in which will
try hard to prevent situations on which files may be corrupted because
of a missinterpretation on how ST works, or just caused by human
distraction.

**Fake Clones**

A fake clone is a file that has been opened in more than one
view/tab/column/group/window and does not share a buffer with the first
instance of it. Changes in one instance of the file opened will
overwrite the other instance, making us lose changes if we don't notice
it.​ Specially happens when we have many windows opened, or when the
amount of opened files is really huge.​ There are a number of situations
on which you may be able to open "fake clones" in the same window. This
package Prevents that.

[1] ​I'm sorry this is not about political corruption.

# Source-code

https://github.com/SublimeText/PreventFakeClones

# Forum Thread​​

http://www.sublimetext.com/forum/viewtopic.php?f=3&t=16019

# License

See license.txt

  [Sublime Text 3+]: http://www.sublimetext.com/
  [Package Control 2+]: https://sublime.wbond.net/installation
