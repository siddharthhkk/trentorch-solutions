# ResNet: The Convolution Output Size

Beginner | research-papers | computer-vision | cnn | architecture

### The problem, from first principles

ResNet (He et al., 2016) opens with a large strided convolution that shrinks the image. Knowing how the spatial size changes at each layer is needed to design such networks and to check their shapes.

### From theory to code

Implement `conv_output_size(n, k, s, p)`, returning the output length of a convolution along one dimension.

### Constraints

- Use integer division.

### Hints

<details>
<summary>Hint 1</summary>

Add the padding on both sides, subtract the kernel, divide by the stride, floor, then add one.

</details>
