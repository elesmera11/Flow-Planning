Minimize
    r
Subject to
    r1: xS1T1D1 + xS1T1D2 + xS1T1D3 + xS2T1D1 + xS2T1D2 + xS2T1D3 + xS3T1D1 + xS3T1D2 + xS3T1D3 - r <= 0
    r2: xS1T2D1 + xS1T2D2 + xS1T2D3 + xS2T2D1 + xS2T2D2 + xS2T2D3 + xS3T2D1 + xS3T2D2 + xS3T2D3 - r <= 0
    r3: xS1T3D1 + xS1T3D2 + xS1T3D3 + xS2T3D1 + xS2T3D2 + xS2T3D3 + xS3T3D1 + xS3T3D2 + xS3T3D3 - r <= 0
    hS1D1: xS1T1D1 + xS1T2D1 + xS1T3D1 = 2
    hS1D2: xS1T1D2 + xS1T2D2 + xS1T3D2 = 3
    hS1D3: xS1T1D3 + xS1T2D3 + xS1T3D3 = 4
    hS2D1: xS2T1D1 + xS2T2D1 + xS2T3D1 = 3
    hS2D2: xS2T1D2 + xS2T2D2 + xS2T3D2 = 4
    hS2D3: xS2T1D3 + xS2T2D3 + xS2T3D3 = 5
    hS3D1: xS3T1D1 + xS3T2D1 + xS3T3D1 = 4
    hS3D2: xS3T1D2 + xS3T2D2 + xS3T3D2 = 5
    hS3D3: xS3T1D3 + xS3T2D3 + xS3T3D3 = 6
    dfS1T1D1: 3 xS1T1D1 - 2 uS1T1D1 = 0
    dfS1T2D1: 3 xS1T2D1 - 2 uS1T2D1 = 0
    dfS1T3D1: 3 xS1T3D1 - 2 uS1T3D1 = 0
    dfS1T1D2: 3 xS1T1D2 - 3 uS1T1D2 = 0
    dfS1T2D2: 3 xS1T2D2 - 3 uS1T2D2 = 0
    dfS1T3D2: 3 xS1T3D2 - 3 uS1T3D2 = 0
    dfS1T1D3: 3 xS1T1D3 - 4 uS1T1D3 = 0
    dfS1T2D3: 3 xS1T2D3 - 4 uS1T2D3 = 0
    dfS1T3D3: 3 xS1T3D3 - 4 uS1T3D3 = 0
    dfS2T1D1: 3 xS2T1D1 - 3 uS2T1D1 = 0
    dfS2T2D1: 3 xS2T2D1 - 3 uS2T2D1 = 0
    dfS2T3D1: 3 xS2T3D1 - 3 uS2T3D1 = 0
    dfS2T1D2: 3 xS2T1D2 - 4 uS2T1D2 = 0
    dfS2T2D2: 3 xS2T2D2 - 4 uS2T2D2 = 0
    dfS2T3D2: 3 xS2T3D2 - 4 uS2T3D2 = 0
    dfS2T1D3: 3 xS2T1D3 - 5 uS2T1D3 = 0
    dfS2T2D3: 3 xS2T2D3 - 5 uS2T2D3 = 0
    dfS2T3D3: 3 xS2T3D3 - 5 uS2T3D3 = 0
    dfS3T1D1: 3 xS3T1D1 - 4 uS3T1D1 = 0
    dfS3T2D1: 3 xS3T2D1 - 4 uS3T2D1 = 0
    dfS3T3D1: 3 xS3T3D1 - 4 uS3T3D1 = 0
    dfS3T1D2: 3 xS3T1D2 - 5 uS3T1D2 = 0
    dfS3T2D2: 3 xS3T2D2 - 5 uS3T2D2 = 0
    dfS3T3D2: 3 xS3T3D2 - 5 uS3T3D2 = 0
    dfS3T1D3: 3 xS3T1D3 - 6 uS3T1D3 = 0
    dfS3T2D3: 3 xS3T2D3 - 6 uS3T2D3 = 0
    dfS3T3D3: 3 xS3T3D3 - 6 uS3T3D3 = 0
    cS1T1: xS1T1D1 + xS1T1D2 + xS1T1D3 - yS1T1 = 0
    cS1T2: xS1T2D1 + xS1T2D2 + xS1T2D3 - yS1T2 = 0
    cS1T3: xS1T3D1 + xS1T3D2 + xS1T3D3 - yS1T3 = 0
    cS2T1: xS2T1D1 + xS2T1D2 + xS2T1D3 - yS2T1 = 0
    cS2T2: xS2T2D1 + xS2T2D2 + xS2T2D3 - yS2T2 = 0
    cS2T3: xS2T3D1 + xS2T3D2 + xS2T3D3 - yS2T3 = 0
    cS3T1: xS3T1D1 + xS3T1D2 + xS3T1D3 - yS3T1 = 0
    cS3T2: xS3T2D1 + xS3T2D2 + xS3T2D3 - yS3T2 = 0
    cS3T3: xS3T3D1 + xS3T3D2 + xS3T3D3 - yS3T3 = 0
    dT1D1: xS1T1D1 + xS2T1D1 + xS3T1D1 - yT1D1 = 0
    dT2D1: xS1T2D1 + xS2T2D1 + xS3T2D1 - yT2D1 = 0
    dT3D1: xS1T3D1 + xS2T3D1 + xS3T3D1 - yT3D1 = 0
    dT1D2: xS1T1D2 + xS2T1D2 + xS3T1D2 - yT1D2 = 0
    dT2D2: xS1T2D2 + xS2T2D2 + xS3T2D2 - yT2D2 = 0
    dT3D2: xS1T3D2 + xS2T3D2 + xS3T3D2 - yT3D2 = 0
    dT1D3: xS1T1D3 + xS2T1D3 + xS3T1D3 - yT1D3 = 0
    dT2D3: xS1T2D3 + xS2T2D3 + xS3T2D3 - yT2D3 = 0
    dT3D3: xS1T3D3 + xS2T3D3 + xS3T3D3 - yT3D3 = 0
    uS1D1: uS1T1D1 + uS1T2D1 + uS1T3D1 = 3
    uS1D2: uS1T1D2 + uS1T2D2 + uS1T3D2 = 3
    uS1D3: uS1T1D3 + uS1T2D3 + uS1T3D3 = 3
    uS2D1: uS2T1D1 + uS2T2D1 + uS2T3D1 = 3
    uS2D2: uS2T1D2 + uS2T2D2 + uS2T3D2 = 3
    uS2D3: uS2T1D3 + uS2T2D3 + uS2T3D3 = 3
    uS3D1: uS3T1D1 + uS3T2D1 + uS3T3D1 = 3
    uS3D2: uS3T1D2 + uS3T2D2 + uS3T3D2 = 3
    uS3D3: uS3T1D3 + uS3T2D3 + uS3T3D3 = 3
Bounds
    xS1T1D1 >= 0
    xS1T2D1 >= 0
    xS1T3D1 >= 0
    xS1T1D2 >= 0
    xS1T2D2 >= 0
    xS1T3D2 >= 0
    xS1T1D3 >= 0
    xS1T2D3 >= 0
    xS1T3D3 >= 0
    xS2T1D1 >= 0
    xS2T2D1 >= 0
    xS2T3D1 >= 0
    xS2T1D2 >= 0
    xS2T2D2 >= 0
    xS2T3D2 >= 0
    xS2T1D3 >= 0
    xS2T2D3 >= 0
    xS2T3D3 >= 0
    xS3T1D1 >= 0
    xS3T2D1 >= 0
    xS3T3D1 >= 0
    xS3T1D2 >= 0
    xS3T2D2 >= 0
    xS3T3D2 >= 0
    xS3T1D3 >= 0
    xS3T2D3 >= 0
    xS3T3D3 >= 0
    cS1T1 >= 0
    cS1T2 >= 0
    cS1T3 >= 0
    cS2T1 >= 0
    cS2T2 >= 0
    cS2T3 >= 0
    cS3T1 >= 0
    cS3T2 >= 0
    cS3T3 >= 0
    dT1D1 >= 0
    dT2D1 >= 0
    dT3D1 >= 0
    dT1D2 >= 0
    dT2D2 >= 0
    dT3D2 >= 0
    dT1D3 >= 0
    dT2D3 >= 0
    dT3D3 >= 0
    r >= 0
Binaries
    uS1T1D1
    uS1T2D1
    uS1T3D1
    uS1T1D2
    uS1T2D2
    uS1T3D2
    uS1T1D3
    uS1T2D3
    uS1T3D3
    uS2T1D1
    uS2T2D1
    uS2T3D1
    uS2T1D2
    uS2T2D2
    uS2T3D2
    uS2T1D3
    uS2T2D3
    uS2T3D3
    uS3T1D1
    uS3T2D1
    uS3T3D1
    uS3T1D2
    uS3T2D2
    uS3T3D2
    uS3T1D3
    uS3T2D3
    uS3T3D3
End