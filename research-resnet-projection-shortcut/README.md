# ResNet: When the Shortcut Needs a Projection

Beginner | research-papers | computer-vision | cnn | architecture

### The problem, from first principles

The identity shortcut adds a block's input to its output. That works only when the shapes match. When the channel count or spatial size changes, ResNet uses a 1x1 projection on the shortcut so the addition is valid.

### From theory to code

Implement `needs_projection(c_in, c_out, stride)`, returning True when the shortcut cannot be an identity.

### Constraints

- Returns a bool.

### Hints

<details>
<summary>Hint 1</summary>

Compare the channel counts and check whether the stride is 1.

</details>
