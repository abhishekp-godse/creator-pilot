import React from 'react';
import { Sparkles, Mic, BarChart3, Target, Calendar } from 'lucide-react';

export function Navbar({ onOpenCoach, onOpenTitleScorer, onOpenWeeklyPlan }) {
  return (
    <header className="sticky top-0 z-40 bg-[#0f172a]/90 backdrop-blur-md border-b border-slate-800 px-6 py-3.5">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        {/* Brand */}
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-600 via-indigo-500 to-emerald-400 flex items-center justify-center shadow-lg shadow-indigo-500/20">
            <Sparkles className="w-5 h-5 text-white" />
          </div>
          <div>
            <span className="font-extrabold text-xl tracking-tight bg-gradient-to-r from-white via-slate-100 to-indigo-200 bg-clip-text text-transparent">
              CreatorPilot
            </span>
            <span className="ml-2 text-xs font-semibold px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
              AI Coach Active
            </span>
          </div>
        </div>

        {/* Quick Action Buttons */}
        <div className="flex items-center gap-3">
          <button
            onClick={onOpenTitleScorer}
            className="flex items-center gap-2 px-3.5 py-1.5 rounded-lg bg-slate-800/80 hover:bg-slate-700/80 text-slate-200 text-sm font-medium border border-slate-700/60 transition shadow-sm"
          >
            <BarChart3 className="w-4 h-4 text-indigo-400" />
            Title Scorer
          </button>

          <button
            onClick={onOpenWeeklyPlan}
            className="flex items-center gap-2 px-3.5 py-1.5 rounded-lg bg-slate-800/80 hover:bg-slate-700/80 text-slate-200 text-sm font-medium border border-slate-700/60 transition shadow-sm"
          >
            <Calendar className="w-4 h-4 text-emerald-400" />
            Weekly Plan
          </button>

          <button
            onClick={onOpenCoach}
            className="flex items-center gap-2 px-4 py-2 rounded-xl bg-gradient-to-r from-indigo-600 to-violet-600 hover:from-indigo-500 hover:to-violet-500 text-white text-sm font-semibold shadow-md shadow-indigo-600/30 transition transform active:scale-95"
          >
            <Mic className="w-4 h-4 animate-pulse text-indigo-200" />
            Talk to AI Coach
          </button>
        </div>
      </div>
    </header>
  );
}
