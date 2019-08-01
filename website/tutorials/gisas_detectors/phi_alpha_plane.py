import ROOT


def hold_root_graphics():
    """
    Holds ROOT graphics while listening to ctr-C event
    """
    Interrupt = False
    while not Interrupt:
        Interrupt = ROOT.gSystem.ProcessEvents()
        ROOT.gSystem.Sleep(10)





c1 = ROOT.TCanvas("c1","c1",1024, 600)
c1.Draw()
c1.cd()
ROOT.gPad.SetLeftMargin(0.1)
ROOT.gPad.SetRightMargin(0.05)
ROOT.gPad.SetTopMargin(0.05)
ROOT.gPad.SetBottomMargin(0.1)

nbinx = 20
xmin = -1.0
xmax = 1.0
dx = (xmax-xmin)/nbinx
nbiny = 10
ymin = 0.0
ymax = 1.0
dy = (ymax-ymin)/nbiny
print dx,dy

h2 = ROOT.TH2D("h2","h2", nbinx, xmin, xmax, nbiny, ymin, ymax)
h2.SetTitle("")
h2.SetStats(0)

h2.GetXaxis().SetTitle("#phi")
h2.GetXaxis().SetTitleSize(0.06)
h2.GetXaxis().SetTitleOffset(0.8)

h2.GetYaxis().SetTitle("#alpha")
h2.GetYaxis().SetTitleSize(0.06)
h2.GetYaxis().SetTitleOffset(0.6)

h2.GetYaxis().SetNdivisions(508)
h2.Draw()

line = ROOT.TLine()
line.SetLineStyle(2)
for nx in range(0, nbinx):
    line.DrawLine(xmin + dx*nx, ymin, xmin + dx*nx, ymax)

for ny in range(0, nbiny):
    line.DrawLine(xmin, ymin + dy*ny, xmax, ymin + dy*ny)

marker = ROOT.TMarker()
marker.SetMarkerStyle(20)
marker.SetMarkerColor(ROOT.kBlue)
for nx in range(0, nbinx):
    x = xmin + dx/2. + dx*nx
    for ny in range(0, nbiny):
        y = ymin + dy/2. + dy*ny
        marker.DrawMarker(x, y)



c1.Modified()
c1.Update()

hold_root_graphics()


