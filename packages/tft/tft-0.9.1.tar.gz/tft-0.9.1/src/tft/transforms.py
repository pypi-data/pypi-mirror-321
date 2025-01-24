import torch
import einops
import math
from pytorch_wavelets import DWTForward, DWT1DForward, DWTInverse, DWT1DInverse

class WPT1D(torch.nn.Module):
    def __init__(self, wt=DWT1DForward(J=1, mode='periodization', wave='bior4.4'), J=4):
        super().__init__()
        self.wt = wt
        self.J = J

    def analysis_one_level(self,x):
        L, H = self.wt(x)
        X = torch.cat([L.unsqueeze(2),H[0].unsqueeze(2)],dim=2)
        X = einops.rearrange(X, 'b c f ℓ -> b (c f) ℓ')
        return X

    def wavelet_analysis(self, x, J):
        for _ in range(J):
            x = self.analysis_one_level(x)
        return x

    def forward(self, x):
        return self.wavelet_analysis(x, J=self.J)


class IWPT1D(torch.nn.Module):
    def __init__(self, iwt=DWT1DInverse(mode='periodization', wave='bior4.4'), J=4):
        super().__init__()
        self.iwt = iwt
        self.J = J

    def synthesis_one_level(self, X):
        X = einops.rearrange(X, 'b (c f) ℓ -> b c f ℓ', f=2)
        L, H = torch.split(X, [1, 1], dim=2)
        L = L.squeeze(2)
        H = [H.squeeze(2)]
        y = self.iwt((L, H))
        return y

    def wavelet_synthesis(self, x, J):
        for _ in range(J):
            x = self.synthesis_one_level(x)
        return x

    def forward(self, x):
        return self.wavelet_synthesis(x, J=self.J)

class WPT2D(torch.nn.Module):
    def __init__(self, wt=DWTForward(J=1, mode='periodization', wave='bior4.4'), J=4):
        super().__init__()
        self.wt  = wt
        self.J = J
    def analysis_one_level(self,x):
        L, H = self.wt(x)
        X = torch.cat([L.unsqueeze(2),H[0]],dim=2)
        X = einops.rearrange(X, 'b c f h w -> b (c f) h w')
        return X
    def wavelet_analysis(self,x,J):
        for _ in range(J):
            x = self.analysis_one_level(x)
        return x
    def forward(self, x):
        return self.wavelet_analysis(x,J=self.J)

        
class IWPT2D(torch.nn.Module):
    def __init__(self, iwt=DWTInverse(mode='periodization', wave='bior4.4'), J=4):
        super().__init__()
        self.iwt  = iwt
        self.J = J
    def synthesis_one_level(self,X):
        X = einops.rearrange(X, 'b (c f) h w -> b c f h w', f=4)
        L, H = torch.split(X, [1, 3], dim=2)
        L = L.squeeze(2)
        H = [H]
        y = self.iwt((L, H))
        return y
    def wavelet_synthesis(self,x,J):
        for _ in range(J):
            x = self.synthesis_one_level(x)
        return x
    def forward(self, x):
        return self.wavelet_synthesis(x,J=self.J)


def strfft(x: torch.Tensor):
    assert x.dim() == 3, "Input must be (batch, channels, length) for strfft."
    B, C, T = x.shape
    frame_size = int(torch.sqrt(torch.tensor(T, dtype=torch.float)).floor().item())
    if frame_size < 1:
        raise ValueError(f"Computed frame_size < 1 (T={T})")
    remainder = T % frame_size
    if remainder != 0:
        total_pad = frame_size - remainder
        left_pad = total_pad // 2
        right_pad = total_pad - left_pad
    else:
        left_pad = 0
        right_pad = 0
    padder = torch.nn.ReflectionPad1d((left_pad, right_pad))
    x_padded = padder(x)
    T_padded = x_padded.shape[-1]
    n_frames = T_padded // frame_size
    frames = x_padded.view(B, C, n_frames, frame_size)
    X = torch.fft.rfft(frames, dim=-1)
    return X, (left_pad, right_pad, frame_size)


def istrfft(X: torch.Tensor, pad_info: tuple):
    left_pad, right_pad, frame_size = pad_info
    B, C, n_frames, freq_bins = X.shape
    frames = torch.fft.irfft(X, n=frame_size, dim=-1)
    x_padded = frames.reshape(B, C, -1)
    T_padded = x_padded.shape[-1]
    if left_pad + right_pad > 0:
        x_reconstructed = x_padded[..., left_pad : T_padded - right_pad]
    else:
        x_reconstructed = x_padded

    return x_reconstructed


def strfft2(x: torch.Tensor):
    B, C, H, W = x.shape
    frame_size = math.floor(math.sqrt(min(H, W)))
    pad_h = 0 if (H % frame_size == 0) else (frame_size - (H % frame_size))
    pad_w = 0 if (W % frame_size == 0) else (frame_size - (W % frame_size))
    pad_top = pad_h // 2
    pad_bottom = pad_h - pad_top
    pad_left = pad_w // 2
    pad_right = pad_w - pad_left
    padder = torch.nn.ReflectionPad2d((pad_left, pad_right, pad_top, pad_bottom))
    x_padded = padder(x)
    _, _, Hp, Wp = x_padded.shape
    x_blocks = x_padded.reshape(
        B, C,
        Hp // frame_size, frame_size,
        Wp // frame_size, frame_size
    )
    x_blocks = x_blocks.permute(0, 1, 2, 4, 3, 5)
    X_stft = torch.fft.rfft2(x_blocks, dim=(-2, -1))
    pad_sizes = (pad_left, pad_right, pad_top, pad_bottom)
    orig_shape = (H, W)
    return X_stft, frame_size, pad_sizes, orig_shape

def istrfft2(X_stft: torch.Tensor,
             frame_size: int,
             pad_sizes: tuple,
             orig_shape: tuple):
    pad_left, pad_right, pad_top, pad_bottom = pad_sizes
    orig_H, orig_W = orig_shape
    B, C, nH, nW, _, _ = X_stft.shape
    x_blocks = torch.fft.irfft2(X_stft, s=(frame_size, frame_size), dim=(-2, -1))
    x_blocks = x_blocks.permute(0, 1, 2, 4, 3, 5)
    x_padded = x_blocks.reshape(
        B, C,
        nH * frame_size,
        nW * frame_size
    )
    if pad_bottom > 0:
        x_padded = x_padded[:, :, :-pad_bottom, :]
    if pad_right > 0:
        x_padded = x_padded[:, :, :, :-pad_right]
    if pad_top > 0:
        x_padded = x_padded[:, :, pad_top:, :]
    if pad_left > 0:
        x_padded = x_padded[:, :, :, pad_left:]
    x_recovered = x_padded[:, :, :orig_H, :orig_W]
    return x_recovered