import React from 'react';
import { HelpCircle, MessageSquareQuote, ArrowUpRight, AlertTriangle, Play } from 'lucide-react';

export function ContentGapFinder({ gaps, videos, onSelectTopic }) {
  return (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
      {/* 1. Content Gap Finder (Audience Questions) */}
      <div className="bg-[#141d2f]/90 border border-slate-800 rounded-2xl p-6">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2">
            <HelpCircle className="w-5 h-5 text-indigo-400" />
            <h3 className="text-base font-bold text-white">Audience Content Gap Finder</h3>
          </div>
          <span className="text-xs font-semibold px-2 py-0.5 rounded-full bg-indigo-500/10 text-indigo-300 border border-indigo-500/20">
            Mined from Comments
          </span>
        </div>
        <p className="text-xs text-slate-400 mb-4">
          High-frequency viewer questions identified in comments that you haven't covered in a dedicated video.
        </p>

        <div className="space-y-3">
          {gaps && gaps.length > 0 ? (
            gaps.map((gap, idx) => (
              <div
                key={idx}
                className="p-3.5 rounded-xl bg-slate-800/40 border border-slate-700/60 hover:border-indigo-500/50 transition group flex flex-col justify-between"
              >
                <div>
                  <div className="flex items-start justify-between gap-2">
                    <h4 className="font-semibold text-sm text-white group-hover:text-indigo-300 transition">
                      {gap.suggested_title}
                    </h4>
                    <span
                      className={`text-[10px] font-bold px-2 py-0.5 rounded-md ${
                        gap.urgency === 'High'
                          ? 'bg-rose-500/10 text-rose-300 border border-rose-500/20'
                          : 'bg-amber-500/10 text-amber-300 border border-amber-500/20'
                      }`}
                    >
                      {gap.urgency} Demand
                    </span>
                  </div>
                  <div className="flex items-center gap-2 mt-2 text-xs text-slate-400 italic">
                    <MessageSquareQuote className="w-3.5 h-3.5 text-slate-500 shrink-0" />
                    <span className="truncate">"{gap.sample_comment}"</span>
                  </div>
                </div>

                <div className="flex items-center justify-between mt-3 pt-2.5 border-t border-slate-700/40 text-[11px]">
                  <span className="text-slate-400">
                    🔥 Requested by <strong className="text-white">{gap.request_count}+ viewers</strong>
                  </span>
                  <button
                    onClick={() => onSelectTopic && onSelectTopic(gap.suggested_title)}
                    className="flex items-center gap-1 text-indigo-400 hover:text-indigo-300 font-medium transition"
                  >
                    Add to Idea Vault <ArrowUpRight className="w-3 h-3" />
                  </button>
                </div>
              </div>
            ))
          ) : (
            <div className="text-center py-6 text-slate-400 text-sm">No content gaps found.</div>
          )}
        </div>
      </div>

      {/* 2. Recent Videos & Drop-Off Hook Analysis */}
      <div className="bg-[#141d2f]/90 border border-slate-800 rounded-2xl p-6">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2">
            <Play className="w-5 h-5 text-emerald-400" />
            <h3 className="text-base font-bold text-white">Video Retention & Drop-Off Hooks</h3>
          </div>
          <span className="text-xs font-semibold px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-300 border border-emerald-500/20">
            ML Diagnostic
          </span>
        </div>
        <p className="text-xs text-slate-400 mb-4">
          Analyzing where viewers drop off in the first 30 seconds and how to fix your hook.
        </p>

        <div className="space-y-3">
          {videos && videos.length > 0 ? (
            videos.slice(0, 3).map((vid) => {
              const dropPct = Math.round(vid.retention_hook_drop * 100);
              const isHighDrop = dropPct > 35;

              return (
                <div
                  key={vid.video_id}
                  className="p-3.5 rounded-xl bg-slate-800/40 border border-slate-700/60 flex items-start gap-3.5"
                >
                  <img
                    src={vid.thumbnail_url}
                    alt={vid.title}
                    className="w-20 h-14 rounded-lg object-cover shrink-0 border border-slate-700"
                  />
                  <div className="min-w-0 flex-1">
                    <h4 className="text-xs font-bold text-white line-clamp-1">{vid.title}</h4>
                    <div className="flex items-center gap-3 text-[11px] text-slate-400 mt-1">
                      <span>{vid.views.toLocaleString()} views</span>
                      <span>•</span>
                      <span>{vid.likes.toLocaleString()} likes</span>
                      <span>•</span>
                      <span>{vid.published_at}</span>
                    </div>

                    <div className="mt-2 flex items-start gap-1.5 text-[11px] leading-tight">
                      <AlertTriangle
                        className={`w-3.5 h-3.5 shrink-0 mt-0.5 ${
                          isHighDrop ? 'text-amber-400' : 'text-emerald-400'
                        }`}
                      />
                      <div>
                        <span className={isHighDrop ? 'text-amber-300 font-semibold' : 'text-emerald-300 font-semibold'}>
                          {dropPct}% 30s Hook Drop:
                        </span>{' '}
                        <span className="text-slate-300">{vid.drop_reason}</span>
                      </div>
                    </div>
                  </div>
                </div>
              );
            })
          ) : (
            <div className="text-center py-6 text-slate-400 text-sm">No video metrics available.</div>
          )}
        </div>
      </div>
    </div>
  );
}
